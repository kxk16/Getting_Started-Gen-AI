from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv 

load_dotenv()

os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


llm = Ollama(model = "llama3")

app = FastAPI(
    title="langchain Server",
    version="1.0",
    description="A simple API Server"

)

prompt = ChatPromptTemplate.from_messages(["write a poem on the topic {topic} with in 50 words"])

add_routes(
    app,
    prompt|llm,
    path="/poem"

)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port = 8000)