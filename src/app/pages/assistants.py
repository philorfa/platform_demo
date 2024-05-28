import streamlit as st
import sys
from pathlib import Path
from buttons import (
    assistant_list_button,
    assistant_create_button,
    assistant_update_button,
    assistant_delete_button)

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
try:
    from sidebar import sidebar
except (Exception, ):
    raise

st.title("Assistants")
st.caption("Manage your Assistants")

sidebar()

names = [
    'Create Assistant',
    'List Assistants',
    'Update Assistant',
    'Delete Assistant'
]

tab = st.tabs(list(names))

with tab[0]:
    st.header('Create Assistant')
    assistant_create_button()
with tab[1]:
    st.header('List Assistants')
    assistant_list_button()

with tab[2]:
    st.header('Update Assistant')
    assistant_update_button()

with tab[3]:
    st.header('Delete Assistant')
    assistant_delete_button()
