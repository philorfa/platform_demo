import streamlit as st
from api_requests import base_list, base_create, base_update, base_delete
from api_requests import (
    assistant_list,
    assistant_create,
    assistant_update,
    assistant_delete)


def base_list_button():

    if st.button('Show List'):
        code, output = base_list()
        if code == 200:
            st.table(output)
        else:
            st.text(output)


def base_create_button():

    if st.button('Create'):
        code, output = base_create()
        if code == 200:
            st.table(output)
        else:
            st.text(output)


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
                st.table(output)
            else:
                st.text(output)


def base_delete_button():

    kb_id = st.text_input('kb_id', key="2")

    # Button to submit inputs
    if st.button('Delete'):
        if kb_id.strip() == '':
            st.error('kb_id is required')
        else:
            code, output = base_delete(kb_id)
            if code == 200:
                st.table(output)
            else:
                st.text(output)


def assistant_list_button():

    if st.button('Show List'):
        code, output = assistant_list()
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
                st.table(feedback[1])
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
                    st.table(feedback[1])
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
                st.table(output)
            else:
                st.text(output)
