import streamlit as st
from anthropic import Anthropic

# Initialize Anthropic client (set your Claude API key as env variable)
client = Anthropic(api_key="YOUR_CLAUDE_API_KEY")

st.set_page_config(page_title="Claude Chatbot Prototype", page_icon="🤖")

st.title("🤖 AI Chatbot Prototype (Claude)")
st.write("Ask me anything! Powered by Claude AI.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Input box
if prompt := st.chat_input("Type your message..."):
    # Save user input
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Send request to Claude
    response = client.messages.create(
        model="claude-3-sonnet-20240229",  # you can use claude-3-haiku (faster) too
        max_tokens=500,
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state["messages"]]
    )

    reply = response.content[0].text
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)
