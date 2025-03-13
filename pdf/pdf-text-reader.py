#!/usr/bin/env python3
import argparse
import os.path
from pypdf import PdfReader

def main():
    parser=argparse.ArgumentParser(description='Script that extracts machine-readable text from given PDF files.')
    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")
    args=parser.parse_args()

    for pdf in args.paths:
        text_folder_path = pdf.replace(".pdf", "") + "-extracted-text"
        if not os.path.exists(text_folder_path):
            os.makedirs(text_folder_path)
        
        pdf_reader = PdfReader(pdf)
        print("\n--- {} ---".format(pdf))
        page_no = 1
        for page in pdf_reader.pages:
            print("\n--- Page {} ---".format(page_no))
            raw_text = page.extract_text()
            
            # Remove additional whitespace to enable more consistent formatting
            text_only_spaces = ' '.join(raw_text.split())
            # Have one sentence per line
            formatted_text = ".\n".join(text_only_spaces.split('. '))
            
            print(formatted_text)
            page_no += 1

if __name__ == "__main__":
    main()