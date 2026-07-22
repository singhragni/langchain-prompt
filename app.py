from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
from prompt_gen import template


model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
  
)
st.header("Rag Research Tool")

user_topic  =st.selectbox("Select Research Paper",["CHatGPT","GROQ","CLAUDE"])
topic_style = st.selectbox("Select topic style",["Begginer","Intermidate"])





# prompt = template.invoke({
#     'user_topic':user_topic,
#     'topic_style':topic_style
# })


prompt = template.format(
    user_topic=user_topic,
    topic_style=topic_style

)

result = model.invoke(prompt)

if st.button("Submit"):
    st.write(result.content)