import pymupdf4llm

pdf_path = "src/files/43006-pdf.pdf"


def main():
    doc = pymupdf4llm.to_markdown(pdf_path)

    # Save output to text file
    output_path = "src/serial/output_pymupdf4llm.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Output saved to: {output_path}")

    return doc


if __name__ == "__main__":
    main()
