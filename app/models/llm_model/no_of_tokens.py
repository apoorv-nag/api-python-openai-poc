from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model_name='text-ada-001', n=2, best_of=2)

print(llm.get_num_tokens('Tell me a joke'))

