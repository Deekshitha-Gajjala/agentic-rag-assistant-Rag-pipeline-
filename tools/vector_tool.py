from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


sample_docs = [
    Document(
        page_content="Apple was fined $500 million for data privacy violations in 2024.",
        metadata={"source": "legal_db"}
    ),
    Document(
        page_content="Amazon faced a class action lawsuit over employee data collection practices.",
        metadata={"source": "legal_db"}
    ),
    Document(
        page_content="GDPR regulations require companies to store user data within EU borders.",
        metadata={"source": "legal_db"}
    ),
    Document(
        page_content="Meta paid $1.3 billion in privacy fines to Irish regulators in 2023.",
        metadata={"source": "legal_db"}
    ),
    Document(
        page_content="Data breach notifications must be sent within 72 hours under GDPR.",
        metadata={"source": "legal_db"}
    ),
]

vectorstore = None


def get_vectorstore():
    global vectorstore

    if vectorstore is None:

        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        vectorstore = Chroma.from_documents(
            documents=sample_docs,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )

    return vectorstore


def vector_search(query: str):

    store = get_vectorstore()

    results = store.similarity_search(query, k=2)

    if not results:
        return "No relevant documents found."

    return "\n".join(
        [doc.page_content for doc in results]
    )


if __name__ == "__main__":

    result = vector_search(
        "privacy violations and fines"
    )

    print(result)