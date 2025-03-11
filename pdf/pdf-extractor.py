#!/usr/bin/env python3
from pypdf import PdfReader, PdfWriter

import argparse
import os.path

def extract_pdf(file_path, start_page, end_page, output_path):
    reader = PdfReader(file_path)
    
    # Clamp page values such that they are in range of given PDF
    start_page = max(1, min(start_page, len(reader.pages)))
    end_page = max(1, min(end_page, len(reader.pages))) 
    
    writer = PdfWriter()
    # In list of reader, pages begin at 0
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

    extracted_page_count = max(0, end_page - start_page + 1)
    if extracted_page_count > 0:
        with open(output_path, 'wb') as fp:
            writer.write(fp)
        
    print("Extracted {} pages to {}".format(extracted_page_count, output_path))

def main():
    parser=argparse.ArgumentParser(description='Script that can copy pages from a PDF document into a new PDF document.')

    parser.add_argument("path", help="List of paths to PDF files, e.g. '*.pdf'")
    parser.add_argument("-s", "--start", default="1", help="First page to include in extracted PDF (starts with 1).")
    parser.add_argument("-e", "--end", default="1", help="Last page to include in extracted PDF.")
    parser.add_argument("-o", "--output", default="extracted-pdf.pdf", help="File name of the extracted pdf.")

    args=parser.parse_args()

    extract_pdf(args.path, int(args.start), int(args.end), args.output)

if __name__ == "__main__":
    main()