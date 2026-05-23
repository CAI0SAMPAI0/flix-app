import requests
import streamlit as st
from api.config import BASE_URL


class ReviewRepository:
    
    def __init__(self):
        self.__base_url = BASE_URL
        self.__reviews_url = f'{self.__base_url}reviews/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state['token']}'
        }

    def get_reviews(self):
        response = requests.get(
            self.__reviews_url,
            headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        return None

    def create_review(self, review):
        response = requests.post(
            self.__reviews_url,
            headers=self.__headers,
            data=review
        )
        if response.status_code == 201:
            return response.json()
        return None

    def update_review(self, id, review):
        response = requests.put(
            f'{self.__reviews_url}{id}/',
            headers=self.__headers,
            data=review
        )
        if response.status_code == 200:
            return response.json()
        return None

    def delete_review(self, id):
        response = requests.delete(
            f'{self.__reviews_url}{id}/',
            headers=self.__headers
        )
        if response.status_code == 204:
            return True
        return False
        
