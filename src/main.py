from src.ingestion import ingest
from src.retriever import create_retriever
from src.chain import create_rag_chain
from transformers import pipeline

from langchain_huggingface import HuggingFacePipeline

import src.config as config


def main():

    vector_store = ingest()

    retriever = create_retriever(
        vector_store
    )

    pipe = pipeline(
        task="text-generation",
        model=config.LLM_MODEL,
        max_new_tokens=256,
        temperature=0.1,
        do_sample=False,
        return_full_text=False,
    )

    llm = HuggingFacePipeline(
        pipeline=pipe,
    )

    chain = create_rag_chain(
        retriever,
        llm,
    )

    while True:

        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:
            break

        answer = chain.invoke(query)
        
        print("\nAssistant:")
        print(answer)


if __name__ == "__main__":
    main()