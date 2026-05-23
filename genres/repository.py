import requests
import streamlit as st
from api.config import BASE_URL

class GenreRepository:
    
    def __init__(self):
        self.__base_url = BASE_URL
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state['token']}'
        }

    def get_genres(self):
        response = requests.get(
            self.__genres_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        return None

    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre
        )
        if response.status_code == 201:
            return response.json()
        return None

    def update_genre(self, id, genre):
        response = requests.put(
            f'{self.__genres_url}{id}/',
            headers=self.__headers,
            data=genre
        )
        if response.status_code == 200:
            return response.json()
        return None

    def delete_genre(self, id):
        response = requests.delete(
            f'{self.__genres_url}{id}/',
            headers=self.__headers
        )
        if response.status_code == 204:
            return True
        return False
        
