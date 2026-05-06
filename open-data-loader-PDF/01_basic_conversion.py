"""
Demo 01 – Basic PDF Conversion to Multiple Formats

Shows how to convert a single PDF into all supported output formats:
    json, markdown, html, text, pdf (searchable), tagged-pdf

Run:
    python 01_basic_conversion.py
"""

import opendataloader_pdf
from pathlib import Path

OUTPUT_DIR = "output/01_basic_conversion"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def main(input_file: str):
    print("=" * 60)
    print("Basic Conversion to All Formats")
    print("=" * 60)
    print(f"Input : {input_file}")
    print(f"Output: {OUTPUT_DIR}/")
    print()

    print("Converting to: json, markdown, html, text, pdf ...")

    opendataloader_pdf.convert(
        input_path=[input_file],
        output_dir=OUTPUT_DIR,
        format="json,markdown,html,text,pdf",
    )

    print("Done.\n")

    output_files = list(Path(OUTPUT_DIR).rglob("*"))
    output_files = [f for f in output_files if f.is_file()]

    print(f"Generated {len(output_files)} file(s):")
    for f in sorted(output_files):
        size_kb = f.stat().st_size / 1024
        print(f"  {f.relative_to(OUTPUT_DIR):<40} {size_kb:>8.1f} KB")

    print("Conversion complete. Open the output folder to inspect all formats.")


if __name__ == "__main__":
    filename: str = "sample_pdfs/doc-full-plain-text.pdf"
    main(filename)
