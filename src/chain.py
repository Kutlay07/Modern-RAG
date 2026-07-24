from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough


def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )


def create_rag_chain(retriever, llm):
    
    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question based on the context.
        
        Context:
        {context}
        
        Question:
        {question}
        """
    )
    
    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return chain

