"""
Demo 07 – Batch Processing Multiple PDFs

Shows how to process an entire folder of PDFs in a single call.
Also demonstrates using a list of explicit file paths for batch conversion.

opendataloader-pdf processes files concurrently, so batching is
significantly faster than calling convert() one file at a time.

Run:
    python 07_batch_processing.py
"""

import time
import opendataloader_pdf
from pathlib import Path

INPUT_DIR  = "sample_pdfs"
OUTPUT_DIR = "output/07_batch_processing"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Demo 07 – Batch Processing")
print("=" * 60)
print()


# ── Show what's in the input folder ──────────────────────────────────────────

pdf_files = sorted(Path(INPUT_DIR).glob("*.pdf"))
print(f"Found {len(pdf_files)} PDF(s) in '{INPUT_DIR}/':")
for f in pdf_files:
    size_kb = f.stat().st_size / 1024
    print(f"  {f.name:<40} {size_kb:>8.1f} KB")
print()


# ── Approach A: Pass an entire folder ────────────────────────────────────────

folder_out = Path(OUTPUT_DIR) / "from_folder"
folder_out.mkdir(exist_ok=True)

print("Approach A – passing the folder path directly ...")
t0 = time.perf_counter()

opendataloader_pdf.convert(
    input_path=[INPUT_DIR],
    output_dir=str(folder_out),
    format="markdown,json",
)

elapsed = time.perf_counter() - t0
print(f"Completed in {elapsed:.2f}s")
print()


# ── Approach B: Pass an explicit list of files ────────────────────────────────

list_out = Path(OUTPUT_DIR) / "from_list"
list_out.mkdir(exist_ok=True)

print("Approach B – passing an explicit list of file paths ...")
t0 = time.perf_counter()

opendataloader_pdf.convert(
    input_path=[str(f) for f in pdf_files],
    output_dir=str(list_out),
    format="markdown,json",
)

elapsed = time.perf_counter() - t0
print(f"Completed in {elapsed:.2f}s")
print()


# ── Summarise the output ──────────────────────────────────────────────────────

def summarise_output(directory: Path, label: str):
    all_files = [f for f in directory.rglob("*") if f.is_file()]
    by_ext: dict[str, list] = {}
    for f in all_files:
        by_ext.setdefault(f.suffix, []).append(f)

    total_size = sum(f.stat().st_size for f in all_files) / 1024
    print(f"--- {label} ---")
    print(f"  Total files : {len(all_files)}")
    print(f"  Total size  : {total_size:.1f} KB")
    for ext, files in sorted(by_ext.items()):
        print(f"  {ext:<8}: {len(files)} file(s)")
    print()


summarise_output(folder_out, "Approach A output (from folder)")
summarise_output(list_out,   "Approach B output (from list)")


# ── Per-file processing time estimate ────────────────────────────────────────

print("Tip: for very large batches, consider chunking input_path into groups")
print("     to control memory usage, while still benefiting from concurrent processing.")
print()
print("Batch processing demo complete.")
print(f"Output saved in: {OUTPUT_DIR}/")
