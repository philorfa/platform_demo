import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
try:
    from sidebar import sidebar
except (Exception, ):
    raise

sidebar()

st.title("Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{
        "role": "assistant",
        "content": "How can I help you?"
    }]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not st.session_state.password:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
