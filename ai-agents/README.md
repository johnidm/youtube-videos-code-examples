# AI Agents Demo

This repository contains examples of different AI agent implementations using OpenAI and CrewAI.

## Project Overview

This project demonstrates various approaches to implementing AI agents:

1. **OpenAI Response API** - Direct interaction with OpenAI's Response API for PDF question answering
2. **OpenAI Agent SDK** - Using OpenAI's Agent SDK with vector stores for document search
3. **OpenAI Agent SDK with Streamlit** - Web interface for the OpenAI Agent implementation
4. **CrewAI Agent** - Using CrewAI framework for agent implementation with Streamlit interface

## Prerequisites

- Python 3.8+
- OpenAI API Key

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-agents
   ```

2. Install dependencies:
   ```bash
   make install-dependencies
   ```
   
   Or manually:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Running the Examples

### OpenAI Response API

This example demonstrates using OpenAI's Response API to answer questions about a PDF file:

```bash
make openai-response-api
```

Or manually:
```bash
python openai-response-api.py
```

### OpenAI Agent SDK

This example uses OpenAI's Agent SDK with vector stores for document search:

```bash
make openai-agent-sdk
```

Or manually:
```bash
python openai-agent-sdk.py
```

### OpenAI Agent SDK with Streamlit

Web interface for the OpenAI Agent implementation:

```bash
make openai-agent-sdk-streamlit
```

Or manually:
```bash
streamlit run openai-agent-sdk-streamlit.py
```

### CrewAI Agent

Using CrewAI framework for agent implementation with Streamlit interface:

```bash
make crewai-agent
```

Or manually:
```bash
streamlit run crewai-agent.py
```

## Project Structure

- `openai-response-api.py` - OpenAI Response API implementation
- `openai-agent-sdk.py` - OpenAI Agent SDK implementation
- `openai-agent-sdk-streamlit.py` - Streamlit interface for OpenAI Agent
- `crewai-agent.py` - CrewAI implementation with Streamlit
- `knowledge/` - Directory containing PDF files used by the agents
- `requirements.txt` - Python dependencies
- `Makefile` - Shortcuts for running the examples

## Notes

- The examples use a PDF file about "ConstruSummit" for demonstration purposes
- Each implementation showcases different approaches to building AI agents
- The Streamlit interfaces provide a user-friendly way to interact with the agents
