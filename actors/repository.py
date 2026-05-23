import requests
import streamlit as st


class ActorsRepository:
    
    def __init__(self):
        self.__base_url = 'https://caio.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state['token']}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        return None

    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.__headers,
            data=actor
        )
        if response.status_code == 201:
            return response.json()
        return None

    def update_actor(self, id, actor):
        response = requests.put(
            f'{self.__actors_url}{id}/',
            headers=self.__headers,
            data=actor
        )
        if response.status_code == 200:
            return response.json()
        return None

    def delete_actor(self, id):
        response = requests.delete(
            f'{self.__actors_url}{id}/',
            headers=self.__headers
        )
        if response.status_code == 204:
            return True
        return False
        
