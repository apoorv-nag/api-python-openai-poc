from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model_name='text-ada-001', n=2, best_of=2)

joke = llm("Tell me a joke")
print(joke)

"""
Generate: More broadly, you can call it with a list of inputs, getting back a more complete response than just the text.
 This complete response includes things like multiple top responses, as well as LLM provider specific information
"""

llm_result = llm.generate(["Tell me a joke", "Tell me a poem"]*5)
print(len(llm_result.generations))

