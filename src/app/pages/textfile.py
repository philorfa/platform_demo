import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
try:
    from sidebar import sidebar
except (Exception, ):
    raise

st.title("Textfile")
st.caption("Manage your Textfiles")

sidebar()

names = [
    'Create Textfile',
    'Retrieve Textfile',
    'Delete Textfile'
]

tab = st.tabs(list(names))

with tab[0]:
    st.header('Create Textfile')

with tab[1]:
    st.header('Retrive Textfile')

with tab[2]:
    st.header('Delete Textfile')
