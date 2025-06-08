# PDF Data Extraction with OpenAI

This project demonstrates how to extract structured data from PDF files using OpenAI's GPT-4 model. It shows token usage patterns when processing different types of PDFs (plain text and text-based images).

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install openai
```

## Usage

1. Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY=<your-openai-api-key>
```

2. Run the script with a PDF file:
```bash
python main.py 'path/to/your/pdf'
```

## Example Results

### Plain Text PDF (doc-plain-text.pdf)

**Token Usage:**
- Completion tokens: 16
- Prompt tokens: 303
- Total tokens: 319

**Extracted Data:**
- name: 'John'
- email: 'johni@johni.com'

### Text-based Images PDF (doc-text-based-images.pdf)

**Token Usage:**
- Completion tokens: 14
- Prompt tokens: 1075
- Total tokens: 1089

**Extracted Data:**
- name: 'John'
- email: 'johni@due.com'

## Notes

- The token usage varies significantly between plain text PDFs and PDFs containing text-based images
- The model used is GPT-4.1-mini
- The extracted data structure includes name and email fields

## Reference

For more information about token usage with PDF content, see the discussion [OpenAI Community Discussion](https://community.openai.com/t/how-does-openai-charge-tokens-when-sending-pdf-content-in-a-prompt/1280985)

