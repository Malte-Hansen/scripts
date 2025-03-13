#!/usr/bin/env python3
import argparse
import os.path
import pypdf

def replace_author_in_pdf(file_path, author, suffix):
    writer = pypdf.PdfWriter()
    reader = pypdf.PdfReader(file_path)
       
    print("\n---", file_path, "---") 

    found_annotations = 0
    for page in reader.pages:
        if '/Annots' in page:
            for annot in page['/Annots']:
                obj = annot.get_object()
                if '/T' in obj:
                    found_annotations += 1
                    print("Replacing author: " + obj['/T'])
                    obj[pypdf.generic.NameObject('/T')] = pypdf.generic.TextStringObject(author)


    print("Replaced author names with '" + author + "' in", found_annotations, " annotations.")

    # Only content is added, meta data is ignored
    writer.append_pages_from_reader(reader)

    output_pdf_path = file_path.replace(".pdf", suffix + ".pdf")

    # Check if output file would overwrite existing file
    if (os.path.isfile(output_pdf_path) and
        input("Output file '{}'already exists. Overwrite? (y/N)".format(output_pdf_path)) != "y"
        ):
        RED = "\033[91m"
        print(f"{RED}Abort: Output file '{output_pdf_path}' already exits.")
        exit()
    
    # Write edited PDF to disk
    with open(output_pdf_path, 'wb') as fp:
        writer.write(fp)

def main():
    parser=argparse.ArgumentParser(description='Script that replaces the author in all annotations for a given list of PDF files.')

    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")
    parser.add_argument("-a", "--author", default="Anonymous", help="Author entries in annotations will be replaced with this string.")
    parser.add_argument("-s", "--suffix", default="", help="Will be added as suffix to output file name to avoid replacement of original files.")

    args=parser.parse_args()

    for file_path in args.paths:
        replace_author_in_pdf(file_path, args.author, args.suffix)

if __name__ == "__main__":
    main()