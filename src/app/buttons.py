import streamlit as st
import uuid
import requests
import os
import pandas as pd
from api_requests import base_list, base_create, base_update, base_delete
from api_requests import (assistant_list, assistant_create, assistant_update,
                          assistant_delete)
from api_requests import (textfile_create, textfile_retrieve, textfile_delete)


def base_list_button():

    if st.button('Show List'):
        code, output = base_list()
        output = pd.DataFrame.from_dict(output)
        if code == 200:
            st.table(output)
        else:
            st.text(output)


def base_create_button():

    if st.button('Create'):
        code, output = base_create()
        # output = pd.DataFrame.from_dict(output)
        if code == 200:
            st.json(output)
        else:
            st.json(output)


def base_update_button():

    kb_id = st.text_input('kb_id', key="1")
    name = st.text_input('Name', value='string')
    description = st.text_input('Description', value='string')

    # Button to submit inputs
    if st.button('Update'):
        if kb_id.strip() == '':
            st.error('kb_id is required')
        else:
            code, output = base_update(kb_id, name, description)
            if code == 200:
                st.json(output)
            else:
                st.json(output)


def base_delete_button():

    kb_id = st.text_input('kb_id', key="2")

    # Button to submit inputs
    if st.button('Delete'):
        if kb_id.strip() == '':
            st.error('kb_id is required')
        else:
            code, output = base_delete(kb_id)
            if code == 200:
                st.json(output)
            else:
                st.json(output)


def assistant_list_button():

    if st.button('Show List'):
        code, output = assistant_list()
        output = pd.DataFrame.from_dict(output)
        if code == 200:
            st.table(output)
        else:
            st.text(output)


def assistant_create_button():

    user_id = st.text_input('user_id', value="0", key="3")
    name = st.text_input('Name', value='string')
    description = st.text_input('Description', value='string')
    model = st.text_input('model', value='string')
    empty_response = st.text_input('empty response', value='string')
    opener = st.text_input('opener', value='string')
    instructions = st.text_input('instructions', value='string')
    similarity_threshold = st.text_input('similarity_threshold',
                                         value='0.5')
    knwoledge_bases = st.text_input("Knowledge bases:", value='0')

    kb_list = knwoledge_bases.split(',')
    kb_list = [int(num.strip()) for num
               in kb_list if num.strip().isdigit()]

    if st.button('Create'):
        feedback = assistant_create(user_id,
                                    name,
                                    description,
                                    model,
                                    empty_response,
                                    opener,
                                    instructions,
                                    similarity_threshold,
                                    kb_list
                                    )
        if len(feedback) == 2:

            if feedback[0] == 200:
                output = pd.DataFrame.from_dict(feedback[1])
                st.table(output)
        else:
            st.text("Please check Input values")


def assistant_update_button():

    a_id = st.text_input('a_id', key="4")

    user_id = st.text_input('user_id', value="0", key="5")
    name = st.text_input('Name', value='string', key="6")
    description = st.text_input('Description', value='string', key="7")
    model = st.text_input('model', value='string', key="8")
    empty_response = st.text_input('empty response', value='string', key="9")
    opener = st.text_input('opener', value='string', key="10")
    instructions = st.text_input('instructions', value='string', key="11")
    similarity_threshold = st.text_input('similarity_threshold',
                                         value='0.5', key="12")
    knwoledge_bases = st.text_input("Knowledge bases:", value='0', key="13")

    kb_list = knwoledge_bases.split(',')
    kb_list = [int(num.strip()) for num
               in kb_list if num.strip().isdigit()]

    if st.button('Update'):
        if a_id.strip() == '':
            st.error('kb_id is required')
        else:
            feedback = assistant_update(a_id,
                                        user_id,
                                        name,
                                        description,
                                        model,
                                        empty_response,
                                        opener,
                                        instructions,
                                        similarity_threshold,
                                        kb_list
                                        )
            if len(feedback) == 2:

                if feedback[0] == 200:
                    output = pd.DataFrame.from_dict(feedback[1])
                    st.table(output)
            else:
                st.text("Please check Input values")


def assistant_delete_button():

    a_id = st.text_input('a_id', key="14")

    # Button to submit inputs
    if st.button('Delete'):
        if a_id.strip() == '':
            st.error('kb_id is required')
        else:
            code, output = assistant_delete(a_id)
            if code == 200:
                st.json(output)
            else:
                st.json(output)


def textfile_create_button():
    kd_id = st.text_input('kd_id', key="15")

    if 'uploaders' not in st.session_state:
        st.session_state.uploaders = []
    if 'uploaded_files' not in st.session_state:
        st.session_state.uploaded_files = {}

    def add_uploader():
        new_uploader_id = str(uuid.uuid4())
        st.session_state.uploaders.append(new_uploader_id)
        st.session_state.uploaded_files[new_uploader_id] = None

    def remove_uploader(uploader_id):
        st.session_state.uploaders = [
            uploader for uploader in st.session_state.uploaders
            if uploader != uploader_id
        ]
        st.session_state.uploaded_files.pop(uploader_id, None)

    st.button("Upload Item", on_click=add_uploader)

    for uploader_id in st.session_state.uploaders:
        with st.container():
            uploaded_file = st.file_uploader("Choose a file", key=uploader_id)
            st.markdown("<div style='margin-top: 10px;'></div>",
                        unsafe_allow_html=True)
            if st.button("Remove", key=f"remove_button_{uploader_id}"):
                remove_uploader(uploader_id)
                st.rerun()
            if uploaded_file is not None:
                st.session_state.uploaded_files[uploader_id] = uploaded_file

                # Specify the API endpoint
                api_url = 'http://127.0.0.1:8000/api/v2/knowledge-bases/5/text-files'
                boundary = str(uuid.uuid4())
                headers = {
                    'accept': '*/*',
                    'Authorization': 'Bearer sk_1320fa8b385fc030a751ee9d5939aa81',
                    'Content-Type': f'multipart/form-data; boundary={boundary}'}

                # Save the uploaded file to a specific path
                save_path = os.path.join(os.getcwd(), uploaded_file.name)
                with open(save_path, 'wb') as f:
                    f.write(uploaded_file.read())

                # Ensure file is successfully saved
                if os.path.exists(save_path):
                    files = {'files': (uploaded_file.name,
                                       open(save_path, 'rb'),
                                       'application/pdf')}
                    # Make the POST request
                    response = requests.post(api_url, headers=headers,
                                             files=files)
                    # st.text(response)
                    # # Log request details for debugging
                    # print('Request URL:', response.request.url)
                    # print('Request Headers:', response.request.headers)
                    # print('Request Body:', response.request.body)

                    # Print response from the server
                    print('Response:', response.text)
    if st.button('Create'):
        if kd_id.strip() == '':
            st.error('kb_id is required')
        elif not st.session_state.uploaded_files:
            st.error("At least one file is required")
        else:
            textfile_create(kd_id, st.session_state.uploaded_files)
            # code, output = textfile_create(kd_id,
            #                                st.session_state.uploaded_files)
            # if code == 200:
            #     st.table(output)
            # else:
            #     st.text(output)


def textfile_retrieve_button():
    tf_id = st.text_input('tf_id', key="18")

    # Button to submit inputs
    if st.button('Retrieve'):
        if tf_id.strip() == '':
            st.error('tf_id is required')
        else:
            feedback = textfile_retrieve(tf_id)
            if len(feedback) == 2:

                if feedback[0] == 200:
                    st.json(feedback[1])
            else:
                st.text("Please check Input values")


def textfile_delete_button():
    tf_id = st.text_input('tf_id', key="19")

    # Button to submit inputs
    if st.button('Delete'):
        if tf_id.strip() == '':
            st.error('tf_id is required')
        else:
            code, output = textfile_delete(tf_id)
            if code == 200:
                st.json(output)
            else:
                st.json(output)
