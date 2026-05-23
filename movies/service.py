from movies.repository import MoviesRepository
import streamlit as st

class MoviesService:

    def __init__(self):
        self.movies_repo = MoviesRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movies_repo.get_movies()
        st.session_state.movies = movies
        return movies

    def get_movies_name(self):
        if 'movies_name' in st.session_state:
            return st.session_state.movies_name
        movies = self.get_movies()
        movies_name = [movie.get('title') for movie in movies]
        st.session_state.movies_name = movies_name
        return movies_name

    def create_movie(self, movie):
        movie = dict(title=movie.get('title'),
                      description=movie.get('description'))
        movies = self.movies_repo.create_movie(movie)
        st.session_state.movies.append(movies)
        st.session_state.movies_name.append(movies.get('title'))
        return movies

    def update_movie(self, id, movie):
        movie = dict(title=movie.get('title'),
                      description=movie.get('description'))
        movies = self.movies_repo.update_movie(id, movie)
        st.session_state.movies.append(movies)
        st.session_state.movies_name.append(movies.get('title'))
        return movies

    def delete_movie(self, id):
        return self.movies_repo.delete_movie(id)

    def get_movie_stats(self):
        if 'movie_stats' in st.session_state:
            return st.session_state.movie_stats
        movie_stats = self.movies_repo.get_movie_stats()
        st.session_state.movie_stats = movie_stats
        return movie_stats