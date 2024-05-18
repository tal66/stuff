import pymupdf  # PyMuPDF


def _get_page_to_chapter_map(pdf):
    ignore_chapters = {'copyright', 'title page', 'index', 'contents', 'table of contents', 'dedication'}
    toc = pdf.get_toc()
    page_to_chapter = {}
    for item in toc:
        chapter = item[1]
        level = item[0]
        if (level == 1) and chapter.strip().lower() not in ignore_chapters:
            page = item[2]
            page_to_chapter[page] = chapter
    return page_to_chapter


def print_highlights(pdf_path):
    with pymupdf.open(pdf_path) as pdf:
        page_to_chapter = _get_page_to_chapter_map(pdf)

        for page_num in range(len(pdf)):
            page = pdf[page_num]
            if page_num in page_to_chapter:
                print(f"\n\n{page_to_chapter[page_num]}\n")

            for annot in page.annots():
                if annot.type[0] == 8:  # type for highlights
                    quads = annot.vertices
                    highlights = []
                    for i in range(0, len(quads), 4):
                        rect = pymupdf.Rect(quads[i][0], quads[i][1], quads[i + 1][0], quads[i + 3][1])
                        highlights.append(page.get_text("text", clip=rect).strip())

                    print(f"p {page_num + 1}")
                    print(" ".join(highlights))
                    print("----")


if __name__ == '__main__':
    pdf_path = r"book.pdf"
    print_highlights(pdf_path)
