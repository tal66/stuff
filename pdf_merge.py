from PyPDF2 import PdfWriter  # V3.0.1
import os

base_dir = r"c:\pdf"
output_filename = "_merged.pdf"

output_file = f'{base_dir}/{output_filename}'
if os.path.exists(output_file):
    os.remove(output_file)
pdf_files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]


def merge_pdfs_with_bookmarks(pdf_files, output_file):
    print("merging:")
    writer = PdfWriter()
    for i, pdf_file in enumerate(pdf_files):
        print(f"{i + 1}. {pdf_file}")
        with open(pdf_file, "rb") as f:
            filename = os.path.basename(pdf_file).split(".")[0]
            writer.append(pdf_file, f"{filename}")

    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"output: {output_file}")


if __name__ == '__main__':
    if len(pdf_files) == 0:
        print(f"no files in {base_dir}")
        exit(1)
    merge_pdfs_with_bookmarks(pdf_files, output_file)
