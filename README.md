# MedRAG (MedPlus)

A Retrieval-Augmented Generation (RAG) chatbot that answers diabetes-related questions from a source document.

## Overview

MedPlus indexes a diabetes reference PDF, retrieves the passages most relevant to a user's question, and passes them to Mixtral-8x7B-Instruct (via the Together AI API). The prompt instructs the model to answer only from the retrieved context and to decline questions outside it. A Streamlit chat UI and a command-line interface are provided.

## Features

- Chat interface built with Streamlit, plus a CLI mode
- Answers grounded in the supplied diabetes document
- Domain-specific embeddings (`NeuML/pubmedbert-base-embeddings`)
- Prompt that refuses out-of-context questions

## Project Structure

```
MedRAG/
├── data/
│   └── diabetes.pdf        # Source document
├── src/
│   ├── load_data.py        # Load the PDF
│   ├── text_splitter.py    # Chunk documents (300 chars, 50 overlap)
│   ├── vector_store.py     # Embed chunks into Chroma
│   ├── retriever.py        # Load the Chroma index as a retriever
│   ├── build_chain.py      # Prompt template
│   ├── interface.py        # RAG chain, Together AI call, CLI
│   └── streamlit_app.py    # Streamlit UI
├── requirements.txt
├── LICENSE
└── README.md
```

## Setup

Requires Python 3.10+.

```bash
git clone https://github.com/m0han-raj/MedRAG
cd MedRAG
python -m venv env
source env/bin/activate        # Windows: .\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

Set your Together AI API key in the `API_KEY` environment variable:

```bash
export API_KEY=your_api_key_here      # PowerShell: $env:API_KEY = "your_api_key_here"
```

## Usage

Run all commands from the repository root (the PDF path is relative).

Streamlit app:

```bash
streamlit run src/streamlit_app.py
```

Then open http://localhost:8501.

Command line:

```bash
python src/interface.py
```

Note: `src/retriever.py` loads a persisted Chroma index from `chroma_index/`, which is git-ignored and not included in the repository. `src/vector_store.py` builds an index from the PDF chunks but does not currently persist it to that directory, so you need to build and persist the index before querying.

## Tech Stack

Python, Streamlit, LangChain, ChromaDB, Hugging Face / sentence-transformers embeddings, Together AI (Mixtral-8x7B-Instruct-v0.1).

## Disclaimer

For informational purposes only. Always consult a healthcare professional for medical advice.

## License

MIT. See [LICENSE](LICENSE).
