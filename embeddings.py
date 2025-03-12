from langchain_ollama import OllamaEmbeddings


def getEmbedding():
    embeddings = OllamaEmbeddings(
        model="llama3",
    )
    return embeddings
