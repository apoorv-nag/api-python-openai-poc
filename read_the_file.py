from langchain.vectorstores import FAISS
# Faceboook AI Similarity Search

from dotenv import load_dotenv

from extensions import llm

load_dotenv()

from langchain.document_loaders import TextLoader
loader = TextLoader('./apn.txt')
documents = loader.load()

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

from langchain.embeddings import OpenAIEmbeddings
# Embeddings
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(docs, embeddings)

query = "What are the technologies involved?"
docs = db.similarity_search(query)
# print(docs[0].page_content)

from langchain.chains.question_answering import load_qa_chain

# Stuff
chain = load_qa_chain(llm, chain_type="map_rerank")

print(chain.run(input_documents=docs, question=query))