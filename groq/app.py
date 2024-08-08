import streamlit as st
import os
from langchain_community.llms import ollama
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain

from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

if "vector" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings()
    st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")
    st.session_state.document = st.session_state.loader.load()
    st.session_state.doc_split = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200).split_documents(st.session_state.document)
    st.session_state.vectors = FAISS.from_documents(st.session_state.doc_split,st.session_state.embeddings)

st.title("ChatGROQ Demo")
llm = ChatGroq(groq_api_key = groq_api_key, model_name = "llama3-8b-8192")

prompt = ChatPromptTemplate.from_template(""" 
                                            Answer the question based on the provided context only.
                                            Kindly give very accurate responses based on the context.
                                          <context>
                                          {context}
                                          </context>
                                          Questions: {input}"""
                                          )

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = st.session_state.vectors.as_retriever()
retriever_chain = create_retrieval_chain(retriever, document_chain)

intext = st.text_input("Enter your prompt here: ")

if intext:
    response = retriever_chain.invoke({"input": intext})
    st.write(response['answer'])