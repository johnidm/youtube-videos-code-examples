"""
Demo 06 – LangChain Integration for RAG Pipelines

Uses the langchain-opendataloader-pdf package to load PDF documents
into LangChain's Document format, ready for ingestion into a vector store
or any other LangChain retrieval pipeline.

Install extra dependency:
    pip install langchain-opendataloader-pdf langchain

Run:
    python 06_langchain_rag.py
"""

from pathlib import Path

print("=" * 60)
print("Demo 06 – LangChain RAG Integration")
print("=" * 60)
print()

try:
    from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader
except ImportError:
    print("ERROR: langchain-opendataloader-pdf is not installed.")
    print("       Run: pip install langchain-opendataloader-pdf langchain")
    raise SystemExit(1)


INPUT_FILES = [
    "sample_pdfs/sample_document.pdf",
    "sample_pdfs/sample_with_tables.pdf",
]


# ── Load documents ────────────────────────────────────────────────────────────

print("Loading documents via OpenDataLoaderPDFLoader ...")
loader = OpenDataLoaderPDFLoader(
    file_path=INPUT_FILES,
    format="text",
)

documents = loader.load()
print(f"Loaded {len(documents)} document chunk(s).\n")


# ── Inspect each Document ─────────────────────────────────────────────────────

print("--- Document summaries ---")
for i, doc in enumerate(documents, start=1):
    content_preview = doc.page_content[:200].replace("\n", " ")
    print(f"\nDocument {i}:")
    print(f"  page_content ({len(doc.page_content)} chars): {content_preview!r} ...")
    print(f"  metadata: {doc.metadata}")


# ── Show character count per document ────────────────────────────────────────

print()
print("--- Character counts ---")
total_chars = 0
for i, doc in enumerate(documents, start=1):
    n = len(doc.page_content)
    total_chars += n
    print(f"  Document {i}: {n:,} characters")
print(f"  Total      : {total_chars:,} characters")
print()


# ── Simulate a simple keyword search ─────────────────────────────────────────

query = "table extraction"
print(f"--- Simple keyword search for: '{query}' ---")
matches = [
    doc for doc in documents
    if query.lower() in doc.page_content.lower()
]
print(f"Found in {len(matches)} document(s).\n")

for doc in matches:
    idx = doc.page_content.lower().find(query.lower())
    snippet = doc.page_content[max(0, idx - 50): idx + 100].replace("\n", " ")
    source = doc.metadata.get("source", "?")
    print(f"  Source   : {source}")
    print(f"  Snippet  : ...{snippet}...")
    print()


# ── Show how to split for chunking ────────────────────────────────────────────

print("--- Chunking with RecursiveCharacterTextSplitter ---")
try:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    print(f"Split {len(documents)} document(s) into {len(chunks)} chunk(s).")
    print(f"Average chunk size: {sum(len(c.page_content) for c in chunks) // len(chunks)} characters")
    print()
    print("First chunk:")
    print(f"  {chunks[0].page_content[:300]!r}")
    print(f"  metadata: {chunks[0].metadata}")
except ImportError:
    print("langchain text splitter not available. Install langchain for splitting support.")

print()
print("LangChain integration demo complete.")
print("These documents are ready to be added to any LangChain vector store (FAISS, Chroma, etc.).")
