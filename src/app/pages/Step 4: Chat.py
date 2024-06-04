import streamlit as st
import sys
from pathlib import Path
from chatbot import (
    chatbot_interface)

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
try:
    from sidebar import sidebar
except (Exception, ):
    raise

st.title("Threads")
st.caption("Start Chatting")

sidebar()

chatbot_interface()
