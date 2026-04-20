import streamlit as st
from llm.openai import openai


st.set_page_config(page_title="A chatbot to create stories", page_icon="🤖")

st.title("AI Chatbot")

#store chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

# display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# user input 

if prompt := st.chat_input("Ask me anything..."):

    #show user msg
    st.chat_message("user").write(prompt)

    #append prompt to massages history
    st.session_state.messages.append({"role": "user", "content": prompt})

    input= [ {"role": m["role"], "content": m["content"]} for m in st.session_state.messages ]
    
    with st.spinner("Thinking..."):
        reply=openai(input).output[0].content[0].text

    #show assistent msg:
    st.chat_message("assistant").write(reply)
    
    #append assistant msg
    st.session_state.messages.append({"role":"assistant", "content":reply})




