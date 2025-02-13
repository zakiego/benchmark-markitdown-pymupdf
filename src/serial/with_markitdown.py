from markitdown import MarkItDown

pdf_path = "src/files/43006-pdf.pdf"


def main():
    md = MarkItDown()
    text = md.convert(pdf_path)

    # Save output to text file
    output_path = "src/serial/output_markitdown.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text.text_content)
    print(f"Output saved to: {output_path}")

    return text


if __name__ == "__main__":
    main()
