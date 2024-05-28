import streamlit as st
import requests
import os

base_url = 'http://127.0.0.1:8000/api/v2/knowledge-bases'
assistant_url = 'http://127.0.0.1:8000/api/v2/assistants'


def base_list():
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + str(st.session_state.token)
        }
    response = requests.get(base_url, headers=headers)
    return response.status_code, response.json()


def base_create():
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + str(st.session_state.token),
        'Content-Type': 'application/json'
        }
    data = {
        "name": "string",
        "description": "string"
        }
    response = requests.post(base_url, headers=headers, json=data)
    return response.status_code, response.json()


def base_update(kb_id, name="string", description="string"):
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + str(st.session_state.token),
        'Content-Type': 'application/json'
        }
    data = {
        "name": name,
        "description": description
        }
    target_base = os.path.join(base_url, str(kb_id))
    response = requests.put(target_base, headers=headers, json=data)
    return response.status_code, response.json()


def base_delete(kb_id):
    headers = {
        'accept': '*/*',
        'Authorization': 'Bearer ' + str(st.session_state.token)
        }

    target_base = os.path.join(base_url, str(kb_id))
    response = requests.delete(target_base, headers=headers)
    return response.status_code, response.json()


def assistant_list():
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + str(st.session_state.token)
        }
    response = requests.get(assistant_url, headers=headers)
    return response.status_code, response.json()


def assistant_create(user_id,
                     name,
                     description,
                     model,
                     empty_response,
                     opener,
                     instructions,
                     similarity_threshold,
                     kb_list):

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + str(st.session_state.token),
        'Content-Type': 'application/json'
        }
    data = {
        "user_id": user_id,
        "name": name,
        "description": description,
        "model": model,
        "empty_response": empty_response,
        "opener": opener,
        "instructions": instructions,
        "similarity_threshold": float(similarity_threshold),
        "knowledge_bases": kb_list
        }

    response = requests.post(assistant_url, headers=headers, json=data)
    if response.status_code == 200:
        return [response.status_code, response.json()]
    else:
        return [response.status_code]


def assistant_update(a_id,
                     user_id,
                     name,
                     description,
                     model,
                     empty_response,
                     opener,
                     instructions,
                     similarity_threshold,
                     kb_list):

    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + str(st.session_state.token),
        'Content-Type': 'application/json'
        }
    data = {
        "user_id": user_id,
        "name": name,
        "description": description,
        "model": model,
        "empty_response": empty_response,
        "opener": opener,
        "instructions": instructions,
        "similarity_threshold": float(similarity_threshold),
        "knowledge_bases": kb_list
        }

    target_assistant = os.path.join(assistant_url, a_id)
    response = requests.put(target_assistant, headers=headers, json=data)
    if response.status_code == 200:
        return [response.status_code, response.json()]
    else:
        return [response.status_code]


def assistant_delete(a_id):
    headers = {
        'accept': '*/*',
        'Authorization': 'Bearer ' + str(st.session_state.token)
        }

    target_assistant = os.path.join(assistant_url, str(a_id))
    response = requests.delete(target_assistant, headers=headers)
    return response.status_code, response.json()
