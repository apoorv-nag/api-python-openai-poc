import openai
import os
from dotenv import load_dotenv

load_dotenv()
# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load GPT-3 language model
model_engine = "text-davinci-002"
prompt = (
    "Create a vector embedding of all the code files in the current directory using GPT-3.\n\n"
)

# Define function to read file content
def read_file_content(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    return content

# Get all code files in current directory
files = [f for f in os.listdir(".") if os.path.isfile(f) and f.endswith(".py")]

# Concatenate file contents into a single string
code_string = ""
for file in files:
    code_string += read_file_content(file)

# Generate vector embedding using GPT-3
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt + code_string,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract vector embedding from GPT-3 response
embedding = response.choices[0].text

# Print vector embedding
print(embedding)
