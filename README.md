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
uv sync
```

## Usage

1. Activate the environment:
```bash
source .venv/bin/activate
```

2. Start Jupyter:
```bash
jupyter lab
```

3. Navigate to the desired topic folder:
   - `1_Intro/` - Introduction and Prompt Engineering
   - `2_Langchain/` - LangChain frameworks
   - `3_RAG/` - Retrieval Augmented Generation
   - `4_Agents/` - AI Agents and MCP server


## Setup with Docker (Python 3.13)

### Prerequisites
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed

### Installation and Usage

1. Build and start the container:
```bash
docker compose up --build
```

2. Access JupyterLab:
   - Open your browser and navigate to `http://localhost:8888`
   - The codebase is mounted as a volume, so any changes you make locally will be immediately reflected in the container

**Note:** The volume mount ensures that:
- All your notebooks and source code are accessible in the container
- Changes made locally are immediately available in JupyterLab
- No need to rebuild the image when updating code

To run in detached mode (background):
```bash
docker compose up -d --build
```

To stop the container:
```bash
docker compose down
```

## API Configuration

The notebooks support OpenAI API, Google Gemini API, and local Ollama.

### Using .env file (Recommended)

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your API keys:
   - `OPENAI_API_KEY` - Your OpenAI API key (required for OpenAI models)
   - `GOOGLE_API_KEY` - Your Google API key (required for Gemini models)
   - `USE_GEMINI` - Set to `true` or `1` to use Gemini instead of OpenAI

3. When using Docker Compose, the `.env` file will be automatically loaded.

### Using environment variables directly

For local development (uv setup), export the variables:
```bash
export OPENAI_API_KEY="your-key-here"
export GOOGLE_API_KEY="your-google-key-here"
export USE_GEMINI="false"
```

Or configure Ollama locally for offline usage.

When using Docker Compose without a `.env` file, you can set them inline:
```bash
OPENAI_API_KEY="your-key-here" GOOGLE_API_KEY="your-google-key-here" docker compose up
```