import streamlit as st
from openai import OpenAI
import random
import time

# Title of the app
st.title("Hi!")

# Prompt the user to enter their OpenAI API key
api_key = st.text_input("Please enter your OpenRouter API key:", type="password")

# Check if the API key is provided
if api_key:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    # Set default model
    if "llm" not in st.session_state:
        st.session_state["llm"] = "meta-llama/llama-3.2-3b-instruct:free"

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask me something..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["llm"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.warning("API key is required to use this application.")
