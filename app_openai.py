import streamlit as st
from openai import OpenAI

# Initialize OpenAI client (make sure you set your API key)
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

st.set_page_config(page_title="AI Chatbot Prototype", page_icon="🤖")

st.title("🤖 AI Chatbot Prototype")
st.write("Ask me anything! Powered by OpenAI GPT.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Get response from OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # you can upgrade to gpt-4
        messages=st.session_state["messages"]
    )

    reply = response.choices[0].message.content
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)
