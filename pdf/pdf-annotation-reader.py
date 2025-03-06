#!/usr/bin/env python3
# Script that prints content of PDF annotations to stdout
from PyPDF2 import PdfReader
import argparse

def read_annotations_in_pdf(file_path):
    print("\n---", file_path, "---") 

    reader = PdfReader(file_path)

    pageNo = 1
    for page in reader.pages:
        if "/Annots" in page:
            for annot in page["/Annots"]:
                obj = annot.get_object()
                if ("/T" in obj and "/Contents" in obj):
                    print("---")
                    print("{}(page {}): {}".format(obj["/T"], str(pageNo), obj["/Contents"]))
        pageNo += 1

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")

    args=parser.parse_args()

    for file_path in args.paths:
        read_annotations_in_pdf(file_path)

if __name__ == "__main__":
    main()