from langchain.prompts import PromptTemplate

from extensions import llm

prompt = PromptTemplate(
    input_variables=['product'],
    # template = "What is a good name for a company that makes {product}?",
    template="Give function requirements questions regarding requirements of {product}?",
)

# p = prompt.format(product='NFT Marketplace')
p = prompt.format(product='Unity Gaming')

res = llm(p)
print(res)
"""
1. What are the system requirements for the game?
2. Are there any specific hardware requirements for the game?
3. What devices will the game be available on?
4. What platforms will the game be compatible with?
5. What is the expected delivery date for the game?
6. What will be the scope of the gaming controls?
7. What type of visuals and graphics do you expect the game to have?
8. What type of multiplayer capabilities will the game have?
9. What type of gameplay mechanics and dynamics are you looking for?
10. What kind of artificial intelligence (AI) systems will the game utilize?
"""
