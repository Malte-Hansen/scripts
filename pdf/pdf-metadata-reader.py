#!/usr/bin/env python3
from pypdf import PdfReader

import argparse
from datetime import datetime

metadata_keys = ["/Title",
 "/Author",
"/Subject",
"/Keywords",
"/Creator",
"/Producer",
"/CreationDate",
"/ModDate",
# "/Trapped"
]

def read_metadata_in_pdf(file_path):
    print("\n---", file_path, "---") 

    reader = PdfReader(file_path)
    meta = reader.metadata

    print(len(reader.pages), "pages")
    for key in metadata_keys:
        if key in meta:
            formatted_value = meta[key] if key.find("Date") == -1 else datetime.strptime(meta[key][2:14], "%Y%m%d%H%M").strftime("%d.%m.%Y %H:%M")
            print("{}: {}".format(key.replace("/", ""), formatted_value))

def main():
    parser=argparse.ArgumentParser(description='Script that can output metadata for a list of given PDF files.')

    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")

    args=parser.parse_args()

    for file_path in args.paths:
        read_metadata_in_pdf(file_path)

if __name__ == "__main__":
    main()