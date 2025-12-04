# Intro to GenAI - Practical Exercises

This repository contains Jupyter notebooks for learning Generative AI, organized by topics: Introduction, Langchain, RAG, and Agents. Each topic includes both teacher (correction) and student versions with fill-in-the-blank exercises.

## Setup with uv (Python 3.13)

### Prerequisites
- [uv](https://github.com/astral-sh/uv) installed
- Python 3.13 available

### Installation

1. Create and activate a uv environment:
```bash
uv venv --python 3.13
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


## Setup with Docker (Python 3.13)

### Prerequisites
- [Docker](https://www.docker.com/) installed

### Installation and Usage

1. Build the Docker image:
```bash
docker build -t genai-cookbook .
```

2. Run the container with volume mounting (allows local code updates):
```bash
docker run -p 8888:8888 -v $(pwd):/app genai-cookbook
```

On Windows (PowerShell):
```bash
docker run -p 8888:8888 -v ${PWD}:/app genai-cookbook
```

On Windows (CMD):
```bash
docker run -p 8888:8888 -v %cd%:/app genai-cookbook
```

3. Access JupyterLab:
   - Open your browser and navigate to `http://localhost:8888`
   - The codebase is mounted as a volume, so any changes you make locally will be immediately reflected in the container

**Note:** The volume mount (`-v $(pwd):/app`) ensures that:
- All your notebooks and source code are accessible in the container
- Changes made locally are immediately available in JupyterLab
- No need to rebuild the image when updating code

## API Configuration

The notebooks support both OpenAI API and local Ollama. Set your API key:
```bash
export OPENAI_API_KEY="your-key-here"
```

Or configure Ollama locally for offline usage.

When using Docker, you can pass environment variables:
```bash
docker run -p 8888:8888 -v $(pwd):/app -e OPENAI_API_KEY="your-key-here" genai-cookbook
```