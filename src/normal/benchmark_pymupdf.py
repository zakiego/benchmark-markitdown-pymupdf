import pymupdf

pdf_path = "src/files/18779-pdf.pdf"
# pdf_path = "src/files/43006-pdf.pdf"


def main():
    doc = pymupdf.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text


if __name__ == "__main__":
    main()
