# Modern-RAG

A modern Retrieval-Augmented Generation (RAG) implementation built with the LangChain ecosystem.

This project recreates the architecture developed in my **RAG-From-Scratch** repository using production-ready libraries such as LangChain, Hugging Face, and FAISS.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python\&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Store-blue)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-yellow?logo=huggingface)

</p>

---

## Overview

The goal of this repository is **not** to explain how RAG works internally.

Instead, it demonstrates how to build the same architecture using modern production libraries.

For the complete from-scratch implementation (custom loaders, chunker, vector store, retriever, cache, etc.), see my **RAG-From-Scratch** project.

---

## Features

* LangChain-based RAG pipeline
* Recursive document loading
* TXT, PDF, Markdown and HTML support
* Recursive text chunking
* Hugging Face embeddings
* FAISS vector store
* Semantic document retrieval
* Prompt template loading from external files
* Local Hugging Face LLM inference
* Modular project structure

---

## Architecture

```text
Documents
      │
      ▼
Directory Loader
      │
      ▼
Document Loaders
      │
      ▼
Recursive Text Splitter
      │
      ▼
Hugging Face Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Prompt Template
      │
      ▼
Local Hugging Face LLM
      │
      ▼
Answer
```

---

## Project Structure

```text
Modern-RAG
│
├── data/
│   └── documents/
│
├── prompts/
│   ├── prompt_loader.py
│   └── rag.txt
│
├── src/
│   ├── chain.py
│   ├── config.py
│   ├── ingestion.py
│   ├── main.py
│   └── retriever.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Kutlay07/Modern-RAG.git

cd Modern-RAG
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Place your documents inside:

```text
data/documents/
```

Supported formats:

```text
.txt
.pdf
.md
.html
```

Run:

```bash
python -m src.main
```

---

## Tech Stack

* Python
* LangChain
* Hugging Face Transformers
* Hugging Face Embeddings
* FAISS
* PyTorch
* tiktoken
* pypdf
* BeautifulSoup4

---

## Related Project

This repository is the **framework-based implementation** of the architecture developed in my **RAG-From-Scratch** project.

While this project focuses on modern tooling and rapid development, the companion repository explains and implements the underlying RAG architecture from scratch.

---

## Roadmap

### v1.0.0 ✅

* LangChain RAG pipeline
* Multi-format document loading
* Recursive text chunking
* Hugging Face embeddings
* FAISS vector store
* Semantic retrieval
* External prompt templates
* Local Hugging Face LLM

Future improvements may include:

* BM25 retrieval
* Hybrid retrieval
* Cross-encoder reranking
* Query rewriting
* Streaming responses

---

## License

This project is licensed under the MIT License.
