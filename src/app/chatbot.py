import streamlit as st
from api_requests import base_list, chat


def chatbot_interface():

    a_id = st.text_input('assistant_id', key="16")
    st.title("Chatbot")

    question = st.text_input("Ask something",
                             placeholder="How can I help you?")

    # Add functionality to the button using Streamlit's button

    if question:
        if a_id.strip() == '':
            st.error('assistant id is required')
        else:

            if not st.session_state.token:
                st.info("Please add your token key to continue.")
                st.stop()

            _, kb_list = base_list()
            if not kb_list:
                st.error("You must create a knowledge base")
                st.stop()
            else:

                endu_id = kb_list[0]['user_id']
                st.chat_message("user").write(question)
                code, msg = chat(a_id, endu_id, question)
                if code == 200:
                    st.chat_message("assistant").write(msg)
                else:
                    st.error(code)
