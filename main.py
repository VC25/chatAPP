# main.py
import streamlit as st
from openai import OpenAI

def main():
    st.title("Hello! vettri")

    api_key = st.text_input("Please enter your OpenRouter API key:", type="password")

    if api_key:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )

        if "llm" not in st.session_state:
            st.session_state["llm"] = "meta-llama/llama-3.2-3b-instruct:free"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ask me something..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

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

if __name__ == "__main__":
    main()
