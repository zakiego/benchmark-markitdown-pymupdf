import pymupdf

pdf_path = "src/files/43006-pdf.pdf"


def main():
    doc = pymupdf.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    # Save output to text file
    output_path = "src/serial/output_pymupdf.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Output saved to: {output_path}")

    return text


if __name__ == "__main__":
    main()
