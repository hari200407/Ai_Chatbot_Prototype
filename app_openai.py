import streamlit as st
import time
from openai import OpenAI
from openai.error import RateLimitError, APIError, ServiceUnavailableError

# Initialize OpenAI client (API key should be stored in Streamlit Secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot Prototype")
st.write("Ask me anything! Powered by OpenAI GPT.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# Display chat history (skip system message)
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").markdown(msg["content"])

# Function to safely call OpenAI with retries
def get_openai_response(messages):
    for attempt in range(5):  # retry up to 5 times
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # you can upgrade to gpt-4
                messages=messages
            )
            return response.choices[0].message.content

        except RateLimitError:
            wait_time = 2 ** attempt
            st.warning(f"⚠️ Rate limit hit. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

        except (APIError, ServiceUnavailableError) as e:
            wait_time = 2 ** attempt
            st.warning(f"⚠️ API error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)

    return "❌ Sorry, I'm overloaded. Please try again later."

# User input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Get response safely
    reply = get_openai_response(st.session_state["messages"])

    # Add assistant reply
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").markdown(reply)
