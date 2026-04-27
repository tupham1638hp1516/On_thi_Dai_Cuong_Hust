"""
Script trích xuất toàn bộ nội dung từ Bank.pdf và lưu thành Quetion_Bank_MMT.md
Sử dụng pymupdf4llm để convert PDF -> Markdown chất lượng cao (bảng, danh sách, text).
"""

import pymupdf4llm
import pathlib
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

PDF_PATH = pathlib.Path(__file__).parent / "Bank.pdf"
OUTPUT_PATH = pathlib.Path(__file__).parent / "Quetion_Bank_MMT.md"

def main():
    if not PDF_PATH.exists():
        print(f"[LỖI] Không tìm thấy file: {PDF_PATH}")
        sys.exit(1)

    print(f"[INFO] Đang trích xuất: {PDF_PATH}")
    print("[INFO] Quá trình này có thể mất vài giây...")

    # Sử dụng pymupdf4llm để convert toàn bộ PDF sang Markdown
    # - pages=None  => tất cả trang
    # - table_strategy="lines" => nhận diện bảng qua đường kẻ
    # - graphics_limit=None => không giới hạn đồ họa
    md_text = pymupdf4llm.to_markdown(
        doc=str(PDF_PATH),
        pages=None,
        table_strategy="lines_strict",
        show_progress=True,
    )

    # Thêm header đẹp vào đầu file
    header = (
        "# Ngân Hàng Câu Hỏi – Mạng Máy Tính\n\n"
        "> **Nguồn:** Bank.pdf  \n"
        "> **Trích xuất bởi:** pymupdf4llm  \n\n"
        "---\n\n"
    )

    final_content = header + md_text

    OUTPUT_PATH.write_text(final_content, encoding="utf-8")

    lines = final_content.count("\n")
    chars = len(final_content)
    print(f"\n[HOÀN THÀNH] Đã lưu: {OUTPUT_PATH}")
    print(f"  - Số dòng  : {lines:,}")
    print(f"  - Số ký tự : {chars:,}")

if __name__ == "__main__":
    main()
