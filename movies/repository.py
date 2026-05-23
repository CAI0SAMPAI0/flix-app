import requests
import streamlit as st
from login.service import logout
from api.config import BASE_URL


class MoviesRepository:

    def __init__(self):
        self.__base_url = BASE_URL
        self.__movies_url = f'{self.__base_url}movies/'

    @property
    def __headers(self):
        return {
            'Authorization': f"Bearer {st.session_state.get('token', '')}"
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__headers  # Aqui ele vai chamar a propriedade dinâmica
        )
        if response.status_code == 200:
            return response.json()
        return None

    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__headers,
            data=movie
        )
        if response.status_code == 201:
            return response.json()
        return None

    def update_movie(self, id, movie):
        response = requests.put(
            f'{self.__movies_url}{id}/',
            headers=self.__headers,
            data=movie
        )
        if response.status_code == 200:
            return response.json()
        return None

    def delete_movie(self, id):
        response = requests.delete(
            f'{self.__movies_url}{id}/',
            headers=self.__headers
        )
        if response.status_code == 204:
            return True
        return False

    def get_movie_stats(self):
        response = requests.get(
            f'{self.__movies_url}stats/',
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')