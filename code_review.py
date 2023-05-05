import os
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import openai
import pinecone

load_dotenv()
# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load GPT-3 language model
# model_engine = "text-davinci-002"
model_engine = "text-embedding-ada-002"
prompt = (
    "Create a vector embedding data of all the code files in the current directory.\n\n"
)
from extensions import llm

# Change the path to the root directory of your project
root_dir = os.getcwd()

memory = ConversationBufferMemory()

text_content = ""

counter = 1
# Traverse the root directory and print the contents of each file
for subdir, dirs, files in os.walk(root_dir):
    # Add more folders to ignore here
    if 'node_modules' in dirs or 'node_modules' in subdir:
        continue
    if 'venv' in dirs or 'venv' in subdir:
        continue
    if '.git' in dirs or '.git' in subdir:
        continue

    for file in files:
        # Check if the file is a Python file
        if file.endswith(".py"):
            # Open the file and print its contents
            file_path = os.path.join(subdir, file)
            memory.chat_memory.add_user_message(f"Create a python file named {file} in path {subdir}")

            # print(subdir+file)
            with open(file_path, "r") as f:
                code_content = f.read()
                text_content += code_content
                response = openai.Embedding.create(
                    engine=model_engine,
                    # prompt=prompt + text_content,
                    input=code_content,
                    # max_tokens=2048,
                    # n=1,
                    # stop=None,
                    # temperature=0.5,
                )
                print(response)

                pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment='us-west4-gcp', service_name='default')
                active_indexes = pinecone.list_indexes()

                index = pinecone.Index('apn')
                counter= counter+1
                upsert_response = index.upsert(
                    vectors=[
                        ("vec"+str(counter), response['data'][0]['embedding'], {})
                    ],
                    namespace="text-namespace",
                )

                # print(code_content)
                # memory.chat_memory.add_user_message(f"""Put the Python Code inside the {file} in path {subdir}
                # {code_content}""")



# m = memory.load_memory_variables({})
# print(m)


# print(text_content)

# Generate vector embedding using GPT-3
response = openai.Embedding.create(
    engine=model_engine,
    prompt="Review the code and explain the code",
    input=text_content,
    # max_tokens=2048,
    # n=1,
    # stop=None,
    # temperature=0.5,
)

# Extract vector embedding from GPT-3 response
embedding = response.data

# Print vector embedding
# print(embedding[0]['embedding'])

query_response = index.query(
    namespace="text-namespace",
    top_k=10,
    include_values=True,
    include_metadata=True,
    vector=embedding[0]['embedding']
)
print(query_response)
# conversation = ConversationChain(llm=llm, verbose=True, memory=memory)
# print(conversation.predict(input="Do a detailed code review and find tell other methods which i can implement other than list_openai_models."))
