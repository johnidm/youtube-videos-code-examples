# open-data-loader-PDF

Code examples for using [opendataloader-pdf](https://pypi.org/project/opendataloader-pdf/) — a Python library for converting and extracting structured data from PDF files.

## Setup

```bash
pip install -r requirements.txt
```

## Examples

| File | Description |
|------|-------------|
| `01_basic_conversion.py` | Convert a PDF to JSON, Markdown, HTML, text, and searchable PDF |
| `02_json_structured_data.py` | Parse JSON output to access elements, bounding boxes, and page metadata |
| `03_table_extraction.py` | Extract tables using border-based or cluster-based detection |
| `04_selective_pages.py` | Process specific pages and preserve original line breaks |
| `05_sanitization.py` | Mask PII (emails, phones, credit cards, IPs) before extraction |
| `06_langchain_rag.py` | Load PDFs into LangChain Documents for RAG pipelines |
| `07_batch_processing.py` | Process an entire folder of PDFs concurrently in one call |

## Running an example

```bash
python 01_basic_conversion.py
```

Each script is self-contained and writes its output to an `output/` subdirectory. Sample PDFs are in `sample_pdfs/`.
