import os
from secretkey import firstkey
from langchain_community.llms import OpenAI

os.environ['OPENAI_API_KEY'] = firstkey

# OPEN_API_KEY = os.getenv('OPEN_API_KEY')

# llm = openai(temperature = 0.6)
# response = llm("Gimme some fancy names for an Indian restaurant")
# print(response)

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9, max_tokens=500)
response = llm("Gimme some fancy names for an Indian restaurant")  # Assuming 'generate_text' is the desired method
print(response)
