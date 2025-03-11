#!/usr/bin/env python3
# Script that can merge multiple PDF files into one
import argparse
import os.path
import pypdf

def main():
    parser=argparse.ArgumentParser(description='Script that can merge multiple given PDF files into one.')

    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")
    parser.add_argument("--output", default="output.pdf", help="File name of merged PDF (output)")

    args=parser.parse_args()

    pdf_writer = pypdf.PdfWriter()

    for pdf in args.paths:
        pdf_reader = pypdf.PdfReader(pdf)
        print("Add", pdf, "to merged file.")

        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    # Check if output file would overwrite existing file
    if (os.path.isfile(args.output) and
        input("Output file '{}' already exists. Overwrite? (y/N)".format(args.output)) != "y"
        ):
        RED = "\033[91m"
        print(f"{RED}Abort: Output file '{args.output}' already exits.")
        exit()

    # Write merged PDF file to disk
    with open(args.output, 'wb') as out_file:
        pdf_writer.write(out_file)

    print("---")
    print("Merged PDF saved as:", args.output)

if __name__ == "__main__":
    main()