"""
https://pymupdf.readthedocs.io/

https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_textpage_ocr

pip install --upgrade pymupdf
"""
import fitz  # PyMuPDF
import sys

def main(pdf_document):
    with fitz.open(pdf_document) as doc:

        for page_number in range(len(doc)):
            page = doc[page_number]
          
            tessdata = "/opt/homebrew/Cellar/tesseract/5.5.0/share/tessdata/"
            tp = page.get_textpage_ocr(language='por', tessdata=tessdata, flags=0, full=False, dpi=300)
            text = page.get_text(textpage=tp, sort=True)

            print(f"Page {page_number + 1}")
            print("---")
            print(text)
            print("\n")

if __name__ == "__main__":
    pdf_document = sys.argv[1]
    main(pdf_document)
