import pymupdf  # PyMuPDF


def copy_bookmarks(src_pdf_path, target_pdf_path, out_pdf_path):
    with pymupdf.open(src_pdf_path) as src_pdf:
        src_toc = src_pdf.get_toc()

    with pymupdf.open(target_pdf_path) as target_pdf:
        target_pdf.set_toc(src_toc)
        target_pdf.save(out_pdf_path)

    print(f"out: {out_pdf_path}")


if __name__ == '__main__':
    # copy bookmarks between files. output to new file.
    # (works ok ignoring warnings about missing keys in pdf)
    src_pdf = "src.pdf"
    target_pdf = "target.pdf"
    out_pdf = "target_with_bookmarks.pdf"
    copy_bookmarks(src_pdf, target_pdf, out_pdf)
