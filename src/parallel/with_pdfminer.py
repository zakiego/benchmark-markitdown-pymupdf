from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from multiprocessing import Pool

pdf_path = "src/files/43006-pdf.pdf"


def process_page_range(args):
    """Process a range of pages from a PDF"""
    start, end = args
    output_string = StringIO()
    with open(pdf_path, "rb") as file:
        parser = PDFParser(file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for i, page in enumerate(PDFPage.create_pages(doc)):
            if start <= i < end:
                interpreter.process_page(page)

    text = output_string.getvalue()
    output_string.close()
    return text


def main():
    # Count total pages
    with open(pdf_path, "rb") as file:
        parser = PDFParser(file)
        doc = PDFDocument(parser)
        total_pages = sum(1 for _ in PDFPage.create_pages(doc))

    num_processes = 8  # Test with different values (2, 4, 8)
    page_ranges = []
    chunk_size = total_pages // num_processes

    # Create page ranges for each process
    for i in range(num_processes):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_processes - 1 else total_pages
        page_ranges.append((start, end))

    with Pool(num_processes) as pool:
        results = pool.map(process_page_range, page_ranges)

    text = "".join(results)

    # Save output to file
    output_file = "src/parallel/output_pdfminer.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    return text


if __name__ == "__main__":
    main()
