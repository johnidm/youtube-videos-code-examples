"""
Demo 04 – Page Selection and Line Break Preservation

Shows two useful extraction options:
    pages           – process only specific pages (e.g. "1", "1,3", "2-4")
    keep_line_breaks – preserve original line breaks in the output text

Run:
    python 04_selective_pages.py
"""

import opendataloader_pdf
from pathlib import Path

INPUT_PDF = "sample_pdfs/sample_document.pdf"
OUTPUT_DIR = "output/04_selective_pages"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Demo 04 – Page Selection & Line Break Preservation")
print("=" * 60)
print()


def convert_and_show(label: str, **kwargs):
    """Run conversion with given kwargs and print a text preview."""
    out = Path(OUTPUT_DIR) / label
    out.mkdir(parents=True, exist_ok=True)

    print(f"--- {label} ---")
    for k, v in kwargs.items():
        if k not in ("input_path", "output_dir", "format"):
            print(f"  {k} = {v!r}")

    opendataloader_pdf.convert(
        input_path=[INPUT_PDF],
        output_dir=str(out),
        format="text,markdown",
        **kwargs,
    )

    txt_files = list(out.rglob("*.txt"))
    if txt_files:
        content = txt_files[0].read_text(encoding="utf-8")
        print(f"  Characters extracted: {len(content)}")
        print(f"  Line count          : {content.count(chr(10))}")
        print()
        preview = content[:600]
        print(preview)
        if len(content) > 600:
            print(f"  ... ({len(content) - 600} more characters)")
    else:
        print("  No text output found.")
    print()


# ── Scenario 1: Full document (default) ──────────────────────────────────────

convert_and_show("full_document")


# ── Scenario 2: Only page 1 ───────────────────────────────────────────────────

convert_and_show("only_page_1", pages="1")


# ── Scenario 3: Pages 1 and 2 ────────────────────────────────────────────────

convert_and_show("pages_1_and_2", pages="1,2")


# ── Scenario 4: Keep line breaks ─────────────────────────────────────────────

convert_and_show("keep_line_breaks", keep_line_breaks=True)


# ── Scenario 5: Page 1 + keep line breaks ────────────────────────────────────

convert_and_show("page_1_with_line_breaks", pages="1", keep_line_breaks=True)


print("Page selection demo complete.")
print(f"Output saved in: {OUTPUT_DIR}/")
