from genres.repository import GenreRepository
import streamlit as st


class GenreService:

    def __init__(self):
        self.genre_repo = GenreRepository()

    def get_genres(self):
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.genre_repo.get_genres()
        st.session_state.genres = genres
        return genres

    def get_genres_name(self):
        if 'genres_name' in st.session_state:
            return st.session_state.genres_name
        genres = self.get_genres()
        genres_name = [genre.get('name') for genre in genres]
        st.session_state.genres_name = genres_name
        return genres_name

    def create_genre(self, genre):
        genre = dict(name=genre)
        genres = self.genre_repo.create_genre(genre)
        st.session_state.genres.append(genres)
        st.session_state.genres_name.append(genres.get('name'))
        return genres

    def update_genre(self, id, genre):
        genre = dict(name=genre)
        genres = self.genre_repo.update_genre(id, genre)
        st.session_state.genres.append(genres)
        st.session_state.genres_name.append(genres.get('name'))
        return genres

    def delete_genre(self, id):
        return self.genre_repo.delete_genre(id)