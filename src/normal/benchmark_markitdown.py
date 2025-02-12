from markitdown import MarkItDown

pdf_path = "src/files/18779-pdf.pdf"
# pdf_path = "src/files/43006-pdf.pdf"


def main():
    md = MarkItDown()
    text = md.convert(pdf_path)
    return text


if __name__ == "__main__":
    main()
