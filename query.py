import json
import os

import pinecone
import requests

from main import PINECONE_API_KEY

pinecone.init(api_key=os.getenv(PINECONE_API_KEY), environment='us-west4-gcp', service_name='default')
active_indexes = pinecone.list_indexes()

index = pinecone.Index("apn")

url = "https://api.openai.com/v1/embeddings"


payload = {
    "model": "text-embedding-ada-002",
    "input": "What is all about queries?",
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + 'sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
}

response = requests.post(url, headers=headers, data=json.dumps(payload)).json()

print(response['data'][0]['embedding'])

pinecone.init(api_key='xx-xx-xx-xx-x', environment='us-west4-gcp', service_name='default')
active_indexes = pinecone.list_indexes()

print(active_indexes)

index = pinecone.Index('apn')

query_response = index.query(
    namespace="645e3679554ef50ac7f3c94f",
    top_k=10,
    include_values=True,
    include_metadata=True,
    vector=response['data'][0]['embedding']
)

print(query_response)

# Get the string from the vector query response

# swap numbers
# print(query_response['matches'][0]['id'])  # example query vector
# print(query_response['matches'][0]['score'])  # example query vector

# print(query_response['matches'][0]['values'].toString())  # example query vector