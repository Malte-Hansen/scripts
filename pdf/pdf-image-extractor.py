#!/usr/bin/env python3
import argparse
import os.path
import pypdf

def main():
    parser=argparse.ArgumentParser(description='Script that extracts images from given PDF files.')

    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")

    args=parser.parse_args()

    for pdf in args.paths:
        image_folder_path = pdf.replace(".pdf", "") + "-extracted-images"
        if not os.path.exists(image_folder_path):
            os.makedirs(image_folder_path)
        
        pdf_reader = pypdf.PdfReader(pdf)
        print("\n--- {} ---".format(pdf))
        pageNo = 1
        for page in pdf_reader.pages:
            count = 0
            for image_file_object in page.images:
                image_file_name = "page-{}-{}-{}".format(pageNo, count, image_file_object.name)
                image_file_path = image_folder_path + "/" + image_file_name
                # Check if output file would overwrite existing file
                if (os.path.isfile(image_file_path) and
                    input("Image file '{}' already exists. Overwrite? (y/N)".format(image_file_path)) != "y"
                    ):
                    break
                with open(image_file_path, "wb") as fp:
                    fp.write(image_file_object.data)
                    count += 1
                    print("Page {}: Wrote image {} to disk.".format(pageNo, image_file_name))
            pageNo += 1

if __name__ == "__main__":
    main()