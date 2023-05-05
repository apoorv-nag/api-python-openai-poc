from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from extensions import llm

from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

prompt = PromptTemplate(
    input_variables=['product'],
    # template = "What is a good name for a company that makes {product}?",
    template="Give function requirements questions regarding requirements of {product}?",
)

# p = prompt.format(product='NFT Marketplace')
# p = prompt.format(product='Unity Gaming')
# p = prompt.format(product='DeFi')
# p = prompt.format(input_language="English", output_language="French", text=p)


# print(llm(p))
# chat = ChatOpenAI(temperature=0)
# conversation = ConversationChain(
#     llm=chat,
#     memory=ConversationBufferMemory()
# )
#
# print(conversation.run("{p}"))


chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run('Defi'))

