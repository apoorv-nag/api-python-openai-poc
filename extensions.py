from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0.9)
