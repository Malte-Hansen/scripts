#!/usr/bin/env python3
import argparse
import os.path
import pypdf

def main():
    parser=argparse.ArgumentParser(description='Script that extracts images from given PDF files.')

    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")

    args=parser.parse_args()

    pdf_writer = pypdf.PdfWriter()

    for pdf in args.paths:
        pdf_reader = pypdf.PdfReader(pdf)
        print("\n--- {} ---".format(pdf))
        count = 0
        for page in range(len(pdf_reader.pages)):
            print("Images:", page.images)
            for image_file_object in page.images:
                image_file_path = str(count) + image_file_object.name
                # Check if output file would overwrite existing file
                if (os.path.isfile(args.output) and
                    input("Image file '{}' already exists. Overwrite? (y/N)".format(image_file_path)) != "y"
                    ):
                    break
                with open(image_file_path, "wb") as fp:
                    fp.write(image_file_object.data)
                    count += 1
                    print("Wrote image {} to disk.".format(image_file_path))

if __name__ == "__main__":
    main()