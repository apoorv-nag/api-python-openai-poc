import json
import os

import redis
import requests
import pinecone

# Connect to Redis
r = redis.Redis(host="xx.xx.xx.xx", password="xxx")

# Subscribe to the "sse" channel
p = r.pubsub()
p.subscribe("sse")

url = "https://api.openai.com/v1/embeddings"


payload = {
    "model": "text-embedding-ada-002",
    "input": "This is a test data of pinecone. different length",
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + 'sk-xx'
}

counter =  1

# Listen for messages
for message in p.listen():
    # Print the message data
    print(message['data'])
    print(message)
    if isinstance(message['data'], int):
        continue
    streamed_data = json.loads(message['data'].decode().strip())

    # Decode the streamed data string and split it into separate lines
    transcript_id = streamed_data['transcript_id'] or None
    message = streamed_data['message'] or None
    print(transcript_id)
    print(message)

    payload = {
        "model": "text-embedding-ada-002",
        "input": message,
    }

    with open('apn.txt', 'a') as outfile:
        # write content to outfile
        outfile.write(message)

    response = requests.post(url, headers=headers, data=json.dumps(payload)).json()

    print(response['data'][0]['embedding'])
    print(len(response['data'][0]['embedding']))

    pinecone.init(api_key='xx-xx-x-x-x', environment='us-west4-gcp', service_name='default')
    active_indexes = pinecone.list_indexes()

    print(active_indexes)

    index = pinecone.Index('apn')

    upsert_response = index.upsert(
        vectors=[
            ("vec2"+str(counter), response['data'][0]['embedding'], {})
        ],
        namespace=f"{transcript_id}",
    )
    counter += 1