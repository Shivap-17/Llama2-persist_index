from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os

#### To persist the data

os.environ["OPENAI_API_KEY"] = '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'
documents = SimpleDirectoryReader("./sleep").load_data()
from llama_index import StorageContext, load_index_from_storage

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