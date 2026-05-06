"""
Generates sample PDF files used across all demo scripts.

Run this first:
    python generate_sample_pdfs.py

Creates:
    sample_pdfs/sample_document.pdf    - multi-page doc with headings & lists
    sample_pdfs/sample_with_tables.pdf - document with structured tables
    sample_pdfs/sample_with_pii.pdf    - document containing PII data
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem
)
from pathlib import Path

OUTPUT_DIR = Path("sample_pdfs")
OUTPUT_DIR.mkdir(exist_ok=True)

styles = getSampleStyleSheet()


# ── Helpers ──────────────────────────────────────────────────────────────────

def h1(text):
    return Paragraph(text, styles["Heading1"])

def h2(text):
    return Paragraph(text, styles["Heading2"])

def h3(text):
    return Paragraph(text, styles["Heading3"])

def p(text):
    return Paragraph(text, styles["Normal"])

def spacer(n=1):
    return Spacer(1, 0.4 * n * cm)


# ── Document 1: General document with headings, paragraphs and lists ─────────

def create_sample_document():
    path = OUTPUT_DIR / "sample_document.pdf"
    doc = SimpleDocTemplate(str(path), pagesize=A4, topMargin=2*cm, bottomMargin=2*cm)

    story = [
        h1("OpenDataLoader PDF – Feature Demo"),
        spacer(),
        p("This document is used to demonstrate the text extraction capabilities of the "
          "opendataloader-pdf library, including reading order, heading hierarchy, "
          "paragraph detection, and list recognition."),
        spacer(),

        h2("1. Introduction"),
        p("PDF documents are widely used for sharing information, but extracting structured "
          "data from them has traditionally been challenging. OpenDataLoader PDF solves this "
          "by providing deterministic, layout-aware extraction powered by the XY-Cut++ algorithm."),
        spacer(),

        h2("2. Key Features"),
        p("The library supports multiple output formats and a range of extraction options:"),
        spacer(0.5),
        ListFlowable([
            ListItem(p("Multi-format output: Markdown, JSON, HTML, plain text, Tagged PDF")),
            ListItem(p("Reading order preserved via XY-Cut++ algorithm")),
            ListItem(p("Heading and list hierarchy detection")),
            ListItem(p("Table extraction (bordered and borderless)")),
            ListItem(p("No GPU required – runs locally")),
        ], bulletType="bullet"),
        spacer(),

        h2("3. Use Cases"),
        p("OpenDataLoader PDF is especially well-suited for AI pipelines:"),
        spacer(0.5),
        ListFlowable([
            ListItem(p("RAG (Retrieval-Augmented Generation) document ingestion")),
            ListItem(p("Legal and compliance document processing")),
            ListItem(p("Scientific paper parsing")),
            ListItem(p("Accessibility auto-tagging")),
        ], bulletType="1"),
        spacer(),

        h2("4. Configuration Options"),
        h3("4.1 Output Formats"),
        p("You can request one or many formats at once by passing a comma-separated string "
          "to the format parameter."),
        spacer(),

        h3("4.2 Page Selection"),
        p("Use the pages parameter to process only specific pages, for example '1,3,5-7'. "
          "This is useful for large documents where you only need a subset."),
        spacer(),

        h2("5. Conclusion"),
        p("OpenDataLoader PDF achieves a 0.907 overall accuracy score, ranking first among "
          "open-source PDF extraction tools. Its hybrid architecture combines AI-based and "
          "deterministic extraction for maximum quality."),
        spacer(),
        p("Page 1 ends here. More content follows on page 2."),
    ]

    # Force page break by adding lots of content
    story += [spacer(5)]
    story += [
        h1("Chapter 2 – Advanced Topics"),
        spacer(),
        h2("2.1 Hybrid Mode"),
        p("Hybrid mode activates AI-powered add-ons: OCR for scanned documents, advanced "
          "table extraction for borderless grids, formula recognition as LaTeX, and chart "
          "analysis with AI-generated descriptions."),
        spacer(),
        h2("2.2 Language Support"),
        p("OCR supports over 80 languages. You can specify language codes when starting the "
          "hybrid backend, for example: --ocr-lang 'pt,en,es'."),
        spacer(),
        h2("2.3 LangChain Integration"),
        p("The langchain-opendataloader-pdf package provides a drop-in document loader for "
          "LangChain pipelines. Documents loaded this way carry page metadata and can be "
          "fed directly into vector stores."),
    ]

    doc.build(story)
    print(f"Created: {path}")


# ── Document 2: Tables ────────────────────────────────────────────────────────

def create_sample_with_tables():
    path = OUTPUT_DIR / "sample_with_tables.pdf"
    doc = SimpleDocTemplate(str(path), pagesize=A4, topMargin=2*cm, bottomMargin=2*cm)

    table_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2C3E50")),
        ("TEXTCOLOR",  (0, 0), (-1, 0), colors.white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("GRID",       (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#ECF0F1")]),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
    ])

    products_data = [
        ["Product",   "Category",  "Price (USD)", "In Stock"],
        ["Laptop Pro", "Electronics", "$1,299.00", "Yes"],
        ["USB-C Hub",  "Accessories", "$49.99",    "Yes"],
        ["Webcam HD",  "Electronics", "$89.00",    "No"],
        ["Desk Mat",   "Office",      "$35.00",    "Yes"],
        ["Monitor 4K", "Electronics", "$649.00",   "Yes"],
    ]

    metrics_data = [
        ["Quarter", "Revenue",    "Users",  "Churn Rate"],
        ["Q1 2024", "$1.2M",      "12,400", "3.2%"],
        ["Q2 2024", "$1.5M",      "15,800", "2.8%"],
        ["Q3 2024", "$1.8M",      "19,200", "2.1%"],
        ["Q4 2024", "$2.1M",      "23,500", "1.9%"],
    ]

    story = [
        h1("Structured Data Extraction – Tables Demo"),
        spacer(),
        p("This document contains multiple tables to demonstrate opendataloader-pdf's "
          "table detection capabilities. Both the default (border-based) and cluster "
          "methods can be tested against these tables."),
        spacer(),

        h2("Product Catalog"),
        p("A simple bordered table with product information:"),
        spacer(0.5),
        Table(products_data, style=table_style, hAlign="LEFT"),
        spacer(),

        h2("Quarterly Business Metrics"),
        p("Financial performance data by quarter:"),
        spacer(0.5),
        Table(metrics_data, style=table_style, hAlign="LEFT"),
        spacer(),

        h2("Feature Comparison"),
        p("Comparison of extraction tool capabilities:"),
        spacer(0.5),
    ]

    comparison_data = [
        ["Feature",              "Tool A", "Tool B", "OpenDataLoader"],
        ["Reading order",        "✓",      "✗",      "✓"],
        ["Table extraction",     "✓",      "✓",      "✓"],
        ["Borderless tables",    "✗",      "✗",      "✓"],
        ["Formula (LaTeX)",      "✗",      "✗",      "✓"],
        ["Tagged PDF output",    "✗",      "✗",      "✓"],
        ["GPU required",         "✓",      "✓",      "✗"],
        ["Accuracy score",       "0.72",   "0.81",   "0.91"],
    ]

    story.append(Table(comparison_data, style=table_style, hAlign="LEFT"))

    doc.build(story)
    print(f"Created: {path}")


# ── Document 3: PII data ──────────────────────────────────────────────────────

def create_sample_with_pii():
    path = OUTPUT_DIR / "sample_with_pii.pdf"
    doc = SimpleDocTemplate(str(path), pagesize=A4, topMargin=2*cm, bottomMargin=2*cm)

    story = [
        h1("Customer Report – Sensitive Data Demo"),
        spacer(),
        p("This document contains personally identifiable information (PII) used to "
          "demonstrate the sanitization feature of opendataloader-pdf."),
        spacer(),

        h2("Customer Contact List"),
        p("Primary contact: <b>Alice Johnson</b>, email: alice.johnson@company.com, "
          "phone: +1 (555) 123-4567"),
        spacer(0.5),
        p("Secondary contact: <b>Bob Smith</b>, email: bob.smith@example.org, "
          "phone: +1 (555) 987-6543"),
        spacer(0.5),
        p("Support engineer: support-team@helpdesk.io, emergency line: 1-800-555-0199"),
        spacer(),

        h2("Payment Information"),
        p("Primary card on file: 4532 1234 5678 9012 (expires 09/27, CVV: 123)"),
        spacer(0.5),
        p("Backup card: 5425 2334 3010 9903 (expires 03/26)"),
        spacer(),

        h2("System Access Logs"),
        p("Last login from IP address: 192.168.1.45 at 2024-03-15 09:32:11 UTC"),
        spacer(0.5),
        p("Failed login attempt from: 10.0.0.254 and 203.0.113.42"),
        spacer(0.5),
        p("Admin access granted to admin@internal.corp from 172.16.254.1"),
        spacer(),

        h2("Personal Details"),
        p("Date of birth: 1985-07-22. SSN: 123-45-6789. "
          "Passport: AB1234567. Driver license: D1234-5678-9012."),
        spacer(),

        h2("Notes"),
        p("All records above are fictional and generated solely for demonstrating "
          "the PII sanitization (--sanitize) capability of opendataloader-pdf. "
          "No real personal data is present in this file."),
    ]

    doc.build(story)
    print(f"Created: {path}")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    create_sample_document()
    create_sample_with_tables()
    create_sample_with_pii()
    print("\nAll sample PDFs created in ./sample_pdfs/")
