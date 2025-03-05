#!/usr/bin/env python3
# Script that can replace authors in PDF annotations, tested with Adobe Acrobat Reader, annotations might disappear for other PDF readers
# Usage example: python3 replace-annotation-authors.py --author=Me --suffix=-edited *.pdf
import PyPDF2
import argparse

def replace_author_in_pdf(file_path, author, suffix):
    writer = PyPDF2.PdfWriter()
    reader = PyPDF2.PdfReader(file_path)
       
    print("\n---", file_path, "---") 

    found_annotations = 0
    for page in reader.pages:
        if '/Annots' in page:
            for annot in page['/Annots']:
                obj = annot.get_object()
                if '/T' in obj:
                    found_annotations += 1
                    print("Replacing author: " + obj['/T'])
                    obj[PyPDF2.generic.NameObject('/T')] = PyPDF2.generic.TextStringObject(author)


    print("Replaced author names with '" + author + "' in", found_annotations, " annotations.")

    # Only content is added, meta data is ignored
    writer.append_pages_from_reader(reader)

    outputPdfFilePath = file_path.replace(".pdf", suffix + ".pdf")
    with open(outputPdfFilePath, 'wb') as fp:
        writer.write(fp)

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")
    parser.add_argument("--author", default="Anonymous", help="Author entries in annotations will be replaced with this string.")
    parser.add_argument("--suffix", default="", help="Will be added as suffix to output file name to avoid replacement of original files.")

    args=parser.parse_args()

    for file_path in args.paths:
        replace_author_in_pdf(file_path, args.author, args.suffix)

if __name__ == "__main__":
    main()