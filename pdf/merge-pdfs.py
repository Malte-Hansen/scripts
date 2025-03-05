# Script that can merge multiple PDF files into one
# Usage example: python3 merge-pdfs.py --output=merged.pdf *.pdf
import PyPDF2
import argparse

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("paths", nargs='+', help="List of paths to PDF files, e.g. '*.pdf'")
    parser.add_argument("--output", default="output.pdf", help="File name of merged PDF (output)")

    args=parser.parse_args()

    pdf_writer = PyPDF2.PdfWriter()

    for pdf in args.paths:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(args.output, 'wb') as out_file:
        pdf_writer.write(out_file)

if __name__ == "__main__":
    main()