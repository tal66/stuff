from pypdf import PdfWriter
import os

base_dir = r"c:\pdf"
output_filename = "_merged.pdf"

output_file = f'{base_dir}/{output_filename}'
if os.path.exists(output_file):
    print(f"rm old out file: {output_file}\n")
    os.remove(output_file)
pdf_files = [os.path.join(base_dir, file) for file in os.listdir(base_dir)]


def merge_pdfs_with_bookmarks(pdf_files, output_file):
    print("merging:")

    writer = PdfWriter()
    i = 1
    for pdf_file in pdf_files:
        if os.path.isdir(pdf_file):
            continue
        if not pdf_file.endswith(".pdf"):
            continue

        print(f"{i}. {pdf_file}")
        filename = os.path.basename(pdf_file).split(".")[0]
        writer.append(pdf_file, f"{filename}")
        i += 1

    with open(output_file, "wb") as f:
        writer.write(f)

    print(f"\noutput: {output_file}\n")


if __name__ == '__main__':
    if len(pdf_files) == 0:
        print(f"no files in {base_dir}")
        exit(1)
    merge_pdfs_with_bookmarks(pdf_files, output_file)
