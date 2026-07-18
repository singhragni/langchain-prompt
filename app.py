from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
  
)


st.header("Rag Research Tool")

input_data = st.text_input("User:")

result = model.invoke(input_data)

st.write(result.content)