import os

import requests
import json

from main import OPENAI_API_KEY, PINECONE_API_KEY

import pinecone


url = "https://api.openai.com/v1/embeddings"


payload = {
    "model": "text-embedding-ada-002",
    "input": "This is a test data of pinecone. different length",
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.getenv(OPENAI_API_KEY)
}

response = requests.post(url, headers=headers, data=json.dumps(payload)).json()

print(response['data'][0]['embedding'])
print(len(response['data'][0]['embedding']))


pinecone.init(api_key=os.getenv(PINECONE_API_KEY), environment='us-west4-gcp', service_name='default')
active_indexes = pinecone.list_indexes()

print(active_indexes)

index = pinecone.Index('apn')

upsert_response = index.upsert(
    vectors=[
        ("vec2", response['data'][0]['embedding'], {})
    ],
    namespace="text-namespace",
)

print(upsert_response)

