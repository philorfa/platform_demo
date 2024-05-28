import streamlit as st


def sidebar():
    st.sidebar.title("Authentication")

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.token = None

    if not st.session_state.authenticated:
        password = st.sidebar.text_input("Enter Token", type="password")
        if st.sidebar.button("Submit"):
            st.session_state.authenticated = True
            st.session_state.token = password
            st.rerun()
    else:
        st.sidebar.success("Token Submitted")
        if st.sidebar.button("Change Token"):
            st.session_state.authenticated = False
            st.session_state.token = None
            st.rerun()
