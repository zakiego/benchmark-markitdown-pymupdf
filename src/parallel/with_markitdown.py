# from multiprocessing import Pool
# from markitdown import MarkItDown, _markitdown


# pdf_path = "src/files/43006-pdf.pdf"

# md = MarkItDown()


# def process_page_range(args):
#     """Process a range of pages from a PDF"""
#     start, end = args
#     doc = md.convert(source=pdf_path, pages=[i for i in range(start, end)])
#     text = ""
#     for page_num in range(start, end):
#         text += doc[page_num].get_text()
#     doc.close()
#     return text


# def main():
#     doc = md.convert(source=pdf_path)
#     total_pages = len(doc)
#     doc.close()

#     num_processes = 16  # Test with different values (2, 4, 8)
#     page_ranges = []
#     chunk_size = total_pages // num_processes

#     # Create page ranges for each process
#     for i in range(num_processes):
#         start = i * chunk_size
#         end = (i + 1) * chunk_size if i != num_processes - 1 else total_pages
#         page_ranges.append((start, end))

#     with Pool(num_processes) as pool:
#         results = pool.map(process_page_range, page_ranges)

#     text = "".join(results)

#     # Save output to file
#     output_file = "src/parallel/output_markitdown.txt"
#     with open(output_file, "w", encoding="utf-8") as f:
#         f.write(text)

#     return text


if __name__ == "__main__":
    # main()
    print("Can't run this file")
