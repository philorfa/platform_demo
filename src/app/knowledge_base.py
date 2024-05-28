import streamlit as st
from sidebar import sidebar
from buttons import (
    base_list_button,
    base_create_button,
    base_update_button,
    base_delete_button)

st.title("Knowledge Bases")
st.caption("Manage your Knowledge Bases")

sidebar()

names = [
    'Create Knowledge Base',
    'List Knowledge Base',
    'Update Knowledge Base',
    'Delete Knowledge Base'
]

tab = st.tabs(list(names))

with tab[0]:
    st.header('Create Knowledge Base')
    base_create_button()

with tab[1]:
    st.header('List Knowledge Base')
    base_list_button()

with tab[2]:
    st.header('Update Knowledge Base')
    base_update_button()

with tab[3]:
    st.header('Delete Knowledge Base')
    base_delete_button()
