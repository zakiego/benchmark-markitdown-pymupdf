from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

pdf_path = "src/files/43006-pdf.pdf"


def main():
    output_string = StringIO()
    with open(pdf_path, "rb") as file:
        parser = PDFParser(file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    text = output_string.getvalue()
    output_string.close()

    # Save output to file
    output_file = "src/serial/output_pdfminer.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    return text


if __name__ == "__main__":
    main()
