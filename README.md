# Intro to GenAI - Practical Exercises

This repository contains Jupyter notebooks for learning Generative AI, organized by topics: Introduction, Langchain, RAG, and Agents. Each topic includes both teacher (correction) and student versions with fill-in-the-blank exercises.

## Setup with uv (Python 3.12)

### Prerequisites
- [uv](https://github.com/astral-sh/uv) installed
- Python 3.12 available

### Installation

1. Create and activate a uv environment:
```bash
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
uv pip install -e .
```

Or install from requirements.txt:
```bash
uv pip install -r requirements.txt
```

## Usage

1. Activate the environment:
```bash
source .venv/bin/activate
```

2. Start Jupyter:
```bash
jupyter notebook
```

3. Navigate to the desired topic folder:
   - `1_Intro/` - Introduction and Prompt Engineering
   - `2_Langchain/` - LangChain frameworks
   - `3_RAG/` - Retrieval Augmented Generation
   - `4_Agents/` - AI Agents and MCP server


## API Configuration

The notebooks support both OpenAI API and local Ollama. Set your API key:
```bash
export OPENAI_API_KEY="your-key-here"
```

Or configure Ollama locally for offline usage.