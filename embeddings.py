import os
from dotenv import load_dotenv, find_dotenv
import pinecone
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "text-embedding-ada-002"
PINECONE_API = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
pinecone.init(api_key=PINECONE_API, environment=PINECONE_ENVIRONMENT)

index_name = "ask-pdf"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, 1526)

index = pinecone.Index(index_name)

