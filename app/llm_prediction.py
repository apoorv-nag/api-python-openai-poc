from langchain.llms import OpenAI

from dotenv import load_dotenv

from extensions import llm

load_dotenv()


text = "Tell a good project on AI"

res = llm(text)

print(res)

# A good project on AI could be creating an AI-driven assistant for financial advisors.
# The AI assistant would be able to assist advisors in their day-to-day activities
# such as portfolio management, research, data analysis, and customer service.
# The AI assistant could use natural language processing, specialized algorithms,
# and machine learning to quickly make decisions and suggest the best course of action for a situation.


