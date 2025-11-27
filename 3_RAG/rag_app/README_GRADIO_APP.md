# 📚 RAG Document Q&A Web App

A Gradio web application that allows you to upload multiple documents (PDF, Word, PPT, TXT) and perform RAG (Retrieval-Augmented Generation) queries using Qdrant as the vector database.

## 🚀 Features

- **Multi-format Document Support**: Upload PDF, Word (.doc, .docx), PowerPoint (.ppt, .pptx), and Text (.txt) files
- **Drag & Drop Interface**: Easy-to-use web interface for document upload
- **Qdrant Vector Database**: Efficient vector storage and similarity search
- **RAG Queries**: Ask questions about your indexed documents and get AI-powered answers
- **Source Citation**: Answers include references to the source documents

## 📋 Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Internet connection (for OpenAI API calls)

## 🔧 Installation

### 1. Install Dependencies

The app requires several Python packages. Install them using one of the following methods:

**Using uv (recommended):**
```bash
uv sync
```

**Using pip:**
```bash
pip install gradio qdrant-client langchain langchain-openai langchain-community pypdf python-docx python-pptx python-dotenv
```

### 2. Set Up OpenAI API Key

You need to set your OpenAI API key as an environment variable. Choose one of the following methods:

**Option A: Environment Variable**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Option B: .env File (Recommended)**
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your-api-key-here
```

The app will automatically load the API key from the `.env` file if `python-dotenv` is installed.

## 🎯 Usage

### Launching the App

1. **Navigate to the project directory:**
   ```bash
   cd rag_app
   ```

2. **Run the Gradio app:**
   ```bash
   python gradio_rag_app.py
   ```

3. **Access the web interface:**
   - The app will start on `http://localhost:7860`
   - Open your web browser and navigate to the URL shown in the terminal
   - You should see the Gradio interface

### Using the App

#### Step 1: Initialize (Automatic)
The system initializes automatically when you launch the app. You should see a status message confirming initialization.

#### Step 2: Upload Documents
1. Click on the file upload area or drag and drop your documents
2. Supported formats:
   - **PDF**: `.pdf`
   - **Word**: `.doc`, `.docx`
   - **PowerPoint**: `.ppt`, `.pptx`
   - **Text**: `.txt`
3. You can upload multiple files at once

#### Step 3: Index Documents
1. After uploading files, click the **"Index Documents"** button
2. Wait for the indexing process to complete
3. You'll see a status message showing:
   - Number of chunks created
   - Files successfully processed
   - Any errors encountered

#### Step 4: Ask Questions
1. Type your question in the "Your Question" text box
2. Click **"Submit"** or press Enter
3. The AI will:
   - Search through your indexed documents
   - Retrieve relevant passages
   - Generate an answer based on the context
   - Show source documents used

#### Step 5: Clear Index (Optional)
- Click **"Clear Index"** to remove all indexed documents and start fresh

## 📖 Example Questions

After indexing documents, try asking:
- "What is the main topic of the documents?"
- "Summarize the key points"
- "What are the important dates mentioned?"
- "Explain [specific concept from your documents]"
- Any question related to the content of your uploaded documents

## 🛠️ Technical Details

### Architecture

- **Vector Database**: Qdrant (in-memory mode for demo)
- **Embeddings**: OpenAI `text-embedding-3-small` (1536 dimensions)
- **LLM**: OpenAI `gpt-4o-mini`
- **Chunking**: RecursiveCharacterTextSplitter (1000 chars, 200 overlap)
- **Retrieval**: Top-4 most relevant chunks per query

### Document Processing

1. **Loading**: Documents are loaded using LangChain document loaders
2. **Chunking**: Documents are split into overlapping chunks for better retrieval
3. **Embedding**: Each chunk is converted to a vector embedding
4. **Indexing**: Embeddings are stored in Qdrant with metadata (source file, etc.)
5. **Retrieval**: Semantic search finds relevant chunks for queries
6. **Generation**: LLM generates answers using retrieved context

### Configuration

You can modify the following in `gradio_rag_app.py`:

- **Chunk size**: Change `chunk_size` in `RecursiveCharacterTextSplitter` (default: 1000)
- **Chunk overlap**: Change `chunk_overlap` (default: 200)
- **Retrieval count**: Change `k` in `search_kwargs` (default: 4)
- **LLM model**: Change `model` in `ChatOpenAI` (default: "gpt-4o-mini")
- **Embedding model**: Change `model` in `OpenAIEmbeddings` (default: "text-embedding-3-small")
- **Qdrant storage**: Change from `:memory:` to a persistent path for data persistence

## 🔍 Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not found"**
   - Make sure you've set the API key as an environment variable or in a `.env` file
   - Restart the app after setting the key

2. **"No relevant documents found"**
   - Make sure you've uploaded and indexed documents before asking questions
   - Try clicking "Index Documents" again

3. **Document loading errors**
   - Check that your file format is supported
   - For Word/PPT files, ensure `python-docx` and `python-pptx` packages are installed
   - Try converting the file to PDF or TXT format if issues persist

4. **Import errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt` or `uv sync`
   - Check Python version (requires 3.11+)

5. **Port already in use**
   - Change the port in `app.launch(server_port=7860)` to a different number

## 📝 Notes

- **In-memory storage**: By default, the Qdrant database is stored in memory, meaning all indexed documents are lost when you restart the app. For persistence, modify the code to use a file path instead of `:memory:`.

- **API costs**: Each query uses OpenAI API calls for both embeddings (if new documents) and LLM generation. Monitor your usage.

- **File size limits**: Very large documents may take time to process. Consider splitting very large files.

- **Privacy**: Documents are processed locally, but embeddings and queries are sent to OpenAI API. Ensure compliance with your data privacy requirements.

## 🔄 Future Enhancements

Potential improvements:
- Persistent Qdrant storage
- Support for more file formats (Excel, HTML, etc.)
- Advanced RAG techniques (reranking, query expansion)
- Document management (view indexed documents, delete specific files)
- Export chat history
- Batch document processing with progress bars

## 🤝 Support

For issues or questions, please refer to the main project documentation or contact the course instructor.

