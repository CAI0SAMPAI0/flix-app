import streamlit as st
from api.service import Auth


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password,
    )
    if response.get('error'):
        st.error(f"Erro ao realizar login: {response.get('error')}")
    else:
        st.session_state.token = response.get('access')
        st.success('Login realizado com sucesso!')
        st.rerun()
    return response


def logout():
    st.session_state.clear()
    st.rerun()