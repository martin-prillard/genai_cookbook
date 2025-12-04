# Use Python 3.13 as base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy pyproject.toml to install dependencies
# Note: Source code will be mounted as a volume at runtime
COPY pyproject.toml .

# Install project dependencies using uv with latest versions
RUN uv pip install --system --no-cache --upgrade -e .


# Expose JupyterLab port
EXPOSE 8888

# Run JupyterLab without password
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]

