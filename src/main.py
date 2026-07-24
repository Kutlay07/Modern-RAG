from src.ingestion import ingest
from src.retriever import create_retriever
from src.chain import create_rag_chain

from langchain_huggingface import HuggingFacePipeline

import src.config as config


def main():

    vector_store = ingest()

    retriever = create_retriever(
        vector_store
    )

    llm = HuggingFacePipeline.from_model_id(
        model_id=config.LLM_MODEL,
        task="text-generation",
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