"""
Demo 03 – Table Extraction

Compares the two available table detection methods:
    default  – border-based detection (fast, best for tables with visible lines)
    cluster  – cluster-based detection (better for borderless/complex tables)

Run:
    python 03_table_extraction.py
"""

import json
import opendataloader_pdf
from pathlib import Path

INPUT_PDF = "sample_pdfs/sample_with_tables.pdf"
OUTPUT_DIR = "output/03_table_extraction"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("Demo 03 – Table Extraction Methods")
print("=" * 60)
print()


def extract_and_show_tables(method: str) -> list:
    """Convert PDF with given table_method and return extracted table elements."""
    out = Path(OUTPUT_DIR) / method
    out.mkdir(parents=True, exist_ok=True)

    print(f"Running with table_method='{method}' ...")
    opendataloader_pdf.convert(
        input_path=[INPUT_PDF],
        output_dir=str(out),
        format="json,markdown",
        table_method=method,
    )

    json_files = list(out.rglob("*.json"))
    if not json_files:
        print(f"  No JSON output for method '{method}'.\n")
        return []

    with open(json_files[0], encoding="utf-8") as f:
        data = json.load(f)

    all_elements = []
    for page in data.get("pages", []):
        all_elements.extend(page.get("elements", []))

    tables = [el for el in all_elements if el.get("type") == "table"]
    print(f"  Found {len(tables)} table(s).\n")
    return tables


# ── Run both methods ──────────────────────────────────────────────────────────

tables_default = extract_and_show_tables("default")
tables_cluster = extract_and_show_tables("cluster")


# ── Compare results ───────────────────────────────────────────────────────────

print("--- Comparison ---")
print(f"  default method : {len(tables_default)} table(s) detected")
print(f"  cluster method : {len(tables_cluster)} table(s) detected")
print()


# ── Inspect each table from the default run ───────────────────────────────────

if tables_default:
    print("--- Tables found with 'default' method ---")
    for i, table in enumerate(tables_default, start=1):
        rows = table.get("rows", [])
        bbox = table.get("bbox", "n/a")
        page = table.get("page", "?")
        print(f"\nTable {i}  (page {page}, bbox={bbox})")
        print(f"  Rows: {len(rows)}")
        for row_idx, row in enumerate(rows):
            cells = row.get("cells", row) if isinstance(row, dict) else row
            cell_texts = [
                (c.get("text", "") if isinstance(c, dict) else str(c))[:20]
                for c in cells
            ]
            print(f"  Row {row_idx}: {cell_texts}")
    print()


# ── Show markdown table output ────────────────────────────────────────────────

md_files = list((Path(OUTPUT_DIR) / "default").rglob("*.md"))
if md_files:
    content = md_files[0].read_text(encoding="utf-8")
    print("--- Markdown output (default method) ---")
    print(content[:2000])
    if len(content) > 2000:
        print(f"... ({len(content) - 2000} more characters)")
    print()

print("Table extraction demo complete.")
print(f"Full output saved in: {OUTPUT_DIR}/")
