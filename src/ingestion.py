from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import BSHTMLLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import src.config as config


def ingest():
    loaders = [
        DirectoryLoader(
            config.DOCUMENTS_PATH,
            glob="**/*.txt",
            loader_cls=TextLoader,
        ),

        DirectoryLoader(
            config.DOCUMENTS_PATH,
            glob="**/*.pdf",
            loader_cls=PyPDFLoader,
        ),

        DirectoryLoader(
            config.DOCUMENTS_PATH,
            glob="**/*.md",
            loader_cls=TextLoader,
        ),

        DirectoryLoader(
            config.DOCUMENTS_PATH,
            glob="**/*.html",
            loader_cls=BSHTMLLoader,
        ),
    ]

    documents = []

    for loader in loaders:
        documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL,
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings,
    )

    return vector_store