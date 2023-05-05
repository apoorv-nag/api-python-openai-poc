import os

import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_ORGANIZATION_KEY = 'OPENAI_ORGANIZATION'
OPENAI_API_KEY = 'OPENAI_API_KEY'
PINECONE_API_KEY = 'PINECONE_API_KEY'


def list_openai_models():
    openai.organization = os.getenv(OPENAI_ORGANIZATION_KEY)
    openai.api_key = os.getenv(OPENAI_API_KEY)
    model_list = openai.Model.list()
    # print(model_list)
    for i in model_list['data']:
        print(i['id'])


if __name__ == '__main__':
    print('List of OpenAI models:')
    list_openai_models()
