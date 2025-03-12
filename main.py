import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate

from populate_data import load_documents, split_documents


def main():


    # Create (or update) the data store.
    documents = load_documents()
    chunks = split_documents(documents)


if __name__ == "__main__":
    main()