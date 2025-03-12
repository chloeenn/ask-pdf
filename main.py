import pinecone
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def load_documents():
    document_loader = PyPDFDirectoryLoader
    return document_loader.load()

def split_document(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ' ', ''],
        chunk_size=1200,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
        return text_splitter.split_documents(documents)

