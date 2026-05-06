"""
Demo 02 – Working with JSON Structured Output

Shows how to parse the JSON output to access:
    - Document elements (headings, paragraphs, lists, images)
    - Bounding boxes for each element
    - Page numbers and font metadata
    - Filtering elements by type

Run:
    python 02_json_structured_data.py
"""

import json
import opendataloader_pdf
from pathlib import Path
from collections import Counter

INPUT_PDF = "sample_pdfs/sample_document.pdf"
OUTPUT_DIR = "output/02_json_structured_data"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Demo 02 – JSON Structured Data Extraction")
print("=" * 60)
print()


# ── Step 1: Convert to JSON ───────────────────────────────────────────────────

print("Converting PDF to JSON ...")
opendataloader_pdf.convert(
    input_path=[INPUT_PDF],
    output_dir=OUTPUT_DIR,
    format="json",
)
print("Done.\n")


# ── Step 2: Load the JSON file ────────────────────────────────────────────────

json_files = list(Path(OUTPUT_DIR).rglob("*.json"))
if not json_files:
    print("No JSON output found. Check that the conversion succeeded.")
    raise SystemExit(1)

json_path = json_files[0]
print(f"Loading: {json_path}")
print()

with open(json_path, encoding="utf-8") as f:
    data = json.load(f)


# ── Step 3: Explore the top-level structure ───────────────────────────────────

print("--- Top-level JSON keys ---")
for key in data.keys():
    value = data[key]
    if isinstance(value, list):
        print(f"  {key}: list with {len(value)} item(s)")
    elif isinstance(value, dict):
        print(f"  {key}: dict with keys {list(value.keys())}")
    else:
        print(f"  {key}: {value!r}")
print()


# ── Step 4: Iterate pages and elements ───────────────────────────────────────

pages = data.get("pages", [])
print(f"Total pages: {len(pages)}")
print()

all_elements = []
for page in pages:
    page_num = page.get("page", "?")
    elements = page.get("elements", [])
    all_elements.extend(elements)
    print(f"Page {page_num}: {len(elements)} element(s)")

print()


# ── Step 5: Count element types ──────────────────────────────────────────────

type_counts = Counter(el.get("type", "unknown") for el in all_elements)
print("--- Element type distribution ---")
for el_type, count in type_counts.most_common():
    print(f"  {el_type:<20} {count:>3}")
print()


# ── Step 6: Show all headings ─────────────────────────────────────────────────

headings = [el for el in all_elements if el.get("type") == "heading"]
if headings:
    print("--- Extracted headings ---")
    for h in headings:
        level = h.get("level", "?")
        text  = h.get("text", "").strip()
        page  = h.get("page", "?")
        print(f"  H{level} (p.{page}): {text}")
    print()


# ── Step 7: Show bounding boxes for first 5 elements ─────────────────────────

print("--- Bounding boxes (first 5 elements, page 1) ---")
page_1_elements = [el for el in all_elements if el.get("page") == 1]
for el in page_1_elements[:5]:
    bbox = el.get("bbox", "n/a")
    el_type = el.get("type", "?")
    text_preview = el.get("text", "")[:50].replace("\n", " ")
    print(f"  type={el_type:<12} bbox={bbox}")
    print(f"    text: {text_preview!r}")
print()


# ── Step 8: Save a filtered subset (only paragraphs) ─────────────────────────

paragraphs_only = [
    {
        "page": el.get("page"),
        "bbox": el.get("bbox"),
        "text": el.get("text", "").strip(),
    }
    for el in all_elements
    if el.get("type") == "paragraph"
]

filtered_path = Path(OUTPUT_DIR) / "paragraphs_only.json"
with open(filtered_path, "w", encoding="utf-8") as f:
    json.dump(paragraphs_only, f, indent=2, ensure_ascii=False)

print(f"Saved {len(paragraphs_only)} paragraph elements to: {filtered_path}")
