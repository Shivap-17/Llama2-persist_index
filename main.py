from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
print(openai_api_key)
# Check if the API key is loaded successfully
if openai_api_key is not None:
    os.environ["OPENAI_API_KEY"] = openai_api_key


#### To persist the data
from llama_index import StorageContext, load_index_from_storage


documents = SimpleDirectoryReader("./sleep").load_data()


try:
    storage_context = StorageContext.from_defaults(persist_dir="./Store")
    index = load_index_from_storage(storage_context)
    print("From Disk")
except:
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir="./Store")
    print("Saving on Disk")

query_engine = index.as_query_engine()
resp = query_engine.query("how much hour should sleep?")
print(resp)