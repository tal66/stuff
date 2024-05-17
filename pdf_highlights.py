import pymupdf  # PyMuPDF


def get_highlights(pdf_path):
    highlights = []
    with pymupdf.open(pdf_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf[page_num]

            for annot in page.annots():
                if annot.type[0] == 8:  # type for highlights
                    text = page.get_text("text", clip=annot.rect)
                    highlights.append({
                        "page": page_num + 1,
                        "highlight": text.strip(),
                    })

    return highlights


def print_highlights(pdf_path):
    highlights = get_highlights(pdf_path)
    for highlight in highlights:
        print(f"p {highlight['page']}")
        print(f"{highlight['highlight']}")
        print("----")


if __name__ == '__main__':
    pdf_path = r"book.pdf"
    print_highlights(pdf_path)
