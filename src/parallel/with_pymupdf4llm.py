import pymupdf4llm
import pymupdf
from multiprocessing import Pool

import pymupdf4llm.helpers

pdf_path = "src/files/43006-pdf.pdf"


def process_page_range(args):
    """Process a range of pages from a PDF"""
    start, end = args
    # Only load the specific pages we need using the pages parameter
    doc = pymupdf4llm.to_markdown(pdf_path, pages=[i for i in range(start, end)])
    text = ""
    for page in doc:
        text += page
    return text


def main():
    # First get total pages using PyMuPDF directly
    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    doc.close()

    num_processes = 16  # Test with different values (2, 4, 8)
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
    output_file = "src/parallel/output_pymupdf4llm.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    return text


if __name__ == "__main__":
    main()
