import os

import requests
import json

from main import OPENAI_API_KEY

url = "https://api.openai.com/v1/completions"


payload = {
    "model": "text-davinci-003",
    "prompt": "This is a test",
    "max_tokens": 50,
    "temperature": 0.9,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.getenv(OPENAI_API_KEY)
}

response = requests.post(url, headers=headers, data=json.dumps(payload)).json()

print(response['choices'][0]['text'])

