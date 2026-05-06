"""
Demo 05 – PII Sanitization

The sanitize option masks personally identifiable information before output:
    - Email addresses
    - Phone numbers
    - Credit card numbers
    - IP addresses

This allows safe extraction of document structure without exposing sensitive data.

Run:
    python 05_sanitization.py
"""

import opendataloader_pdf
from pathlib import Path

INPUT_PDF = "sample_pdfs/sample_with_pii.pdf"
OUTPUT_DIR = "output/05_sanitization"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Demo 05 – PII Sanitization")
print("=" * 60)
print()


# ── Extract WITHOUT sanitization ─────────────────────────────────────────────

raw_dir = Path(OUTPUT_DIR) / "raw"
raw_dir.mkdir(exist_ok=True)

print("Extracting WITHOUT sanitization ...")
opendataloader_pdf.convert(
    input_path=[INPUT_PDF],
    output_dir=str(raw_dir),
    format="text",
    sanitize=False,
)
print("Done.\n")


# ── Extract WITH sanitization ─────────────────────────────────────────────────

sanitized_dir = Path(OUTPUT_DIR) / "sanitized"
sanitized_dir.mkdir(exist_ok=True)

print("Extracting WITH sanitization ...")
opendataloader_pdf.convert(
    input_path=[INPUT_PDF],
    output_dir=str(sanitized_dir),
    format="text",
    sanitize=True,
)
print("Done.\n")


# ── Compare outputs side by side ──────────────────────────────────────────────

raw_files       = list(raw_dir.rglob("*.txt"))
sanitized_files = list(sanitized_dir.rglob("*.txt"))

if not raw_files or not sanitized_files:
    print("Missing output files. Check that conversion succeeded.")
    raise SystemExit(1)

raw_text       = raw_files[0].read_text(encoding="utf-8")
sanitized_text = sanitized_files[0].read_text(encoding="utf-8")

print("=" * 60)
print("ORIGINAL (with PII)")
print("=" * 60)
print(raw_text)

print()
print("=" * 60)
print("SANITIZED (PII masked)")
print("=" * 60)
print(sanitized_text)

print()


# ── Show a quick diff summary ─────────────────────────────────────────────────

raw_lines       = raw_text.splitlines()
sanitized_lines = sanitized_text.splitlines()

changed_lines = 0
for raw_line, san_line in zip(raw_lines, sanitized_lines):
    if raw_line != san_line:
        changed_lines += 1
        print(f"  BEFORE: {raw_line.strip()}")
        print(f"  AFTER : {san_line.strip()}")
        print()

print(f"Lines modified by sanitization: {changed_lines}")
print(f"\nFull output saved in: {OUTPUT_DIR}/")
