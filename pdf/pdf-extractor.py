#!/usr/bin/env python3
from PyPDF2 import PdfReader, PdfWriter

import argparse
import os.path

def extract_pdf(file_path, start_page, end_page, output_path):
    reader = PdfReader(file_path)
    if start_page < 1 or end_page > len(reader.pages):
        RED = "\033[91m"
        print(f"{RED}Abort: Invalid arguments for PDF with '{len(reader.pages)}' pages.")
        exit()
    
    
    writer = PdfWriter()
    # In list, pages begin at 0
    current_page = start_page -1
    while current_page < end_page:
        writer.add_page(reader.pages[current_page])
        current_page+=1

    # Check if output file would overwrite existing file
    if (os.path.isfile(output_path) and
        input("Output file '{}'already exists. Overwrite? (y/N)".format(output_path)) != "y"
        ):
        RED = "\033[91m"
        print(f"{RED}Abort: Output file '{output_path}' already exits.")
        exit()

    with open(output_path, 'wb') as fp:
        writer.write(fp)

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("path", help="List of paths to PDF files, e.g. '*.pdf'")
    parser.add_argument("-s", "--start", default="1", help="First page to include in extracted PDF (start with 1).")
    parser.add_argument("-e", "--end", default="1", help="Last page to include in extracted PDF.")
    parser.add_argument("-o", "--output", default="extracted-pdf.pdf", help="File name of the extracted pdf.")

    args=parser.parse_args()

    extract_pdf(args.path, int(args.start), int(args.end), args.output)

if __name__ == "__main__":
    main()