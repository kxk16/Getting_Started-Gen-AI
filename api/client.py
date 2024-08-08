import requests
import streamlit as st
def llama_get_respomse(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json = {'input':{'topic':input_text}})
    return response.json()['output']

st.title("Langchain Demo with LLama 3 API")
input_text = st.text_input("Write a poem on ")

if input_text:
    st.write(llama_get_respomse(input_text))