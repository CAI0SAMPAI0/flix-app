# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

movies = [
    {'id':1, 'title': 'Titanic', 'genre': 'Romance', 'year': 1997},
    {'id':2, 'title': 'The Lion King', 'genre': 'Animation', 'year': 1994},
    {'id':3, 'title': 'The Matrix', 'genre': 'Sci-Fi', 'year': 1999},
    {'id':4, 'title': 'The Godfather', 'genre': 'Crime', 'year': 1972},
    {'id':5, 'title': 'The Dark Knight', 'genre': 'Action', 'year': 2008}
]

movies_df = pd.DataFrame(movies)

def show_movies():
    st.title('Página de Filmes')

    AgGrid(
        movies_df,
        editable=True,
        key='movies_grid',
    )

    st.title('Adicionar Filme')
    title = st.text_input('Nome do Filme')
    genre = st.text_input('Gênero do Filme')
    year = st.text_input('Ano do Filme')
    if st.button('Adicionar'):
        movies.append({'id': len(movies) + 1, 'title': title, 'genre': genre, 'year': year})
        st.success('Filme adicionado com sucesso!')
        st.rerun()

    st.title('Deletar Filme')
    id_to_delete = st.text_input('ID do Filme')
    if st.button('Deletar'):
        for movie in movies:
            if movie.get('id') == int(id_to_delete):
                movies.remove(movie)
                break
        st.success('Filme deletado com sucesso!')
        st.rerun()

    st.title('Atualizar Filme')
    new_title = st.text_input('Novo Título do Filme')
    new_genre = st.text_input('Novo Gênero do Filme')
    new_year = st.text_input('Novo Ano do Filme')
    if st.button('Atualizar'):
        for movie in movies:
            if movie.get('id') == int(id):
                movie['title'] = new_title
                movie['genre'] = new_genre
                movie['year'] = new_year
                break
        st.success('Filme atualizado com sucesso!')
        st.rerun()