from genres.repository import GenreRepository
from functools import cache
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    # Se a API retornou dados válidos, normaliza. 
    # Se veio None ou vazio, cria um DataFrame vazio com as colunas id e name.
    if genres and isinstance(genres, list):
        genres_df = pd.json_normalize(genres)
    else:
        genres_df = pd.DataFrame(columns=['id', 'name'])

    # Exibe a listagem de Gêneros
    st.title('Página de Gêneros')
    
    if not genres:
        st.info("Nenhum gênero cadastrado no banco de dados ainda.")
        
    AgGrid(
        genres_df,
        editable=True,
        key='genres_grid',
    )

    # --- Daqui para baixo, a página SEMPRE vai aparecer ---
    
    st.title('Adicionar Gênero')
    name = st.text_input('Nome do Gênero')
    if st.button('Adicionar'):
        new_genre = genre_service.create_genre(name)
        if new_genre:
            st.success('Gênero adicionado com sucesso!')
            st.rerun()
        else:
            st.error('Erro ao adicionar gênero. Verifique se o gênero já existe ou se você tem permissão para criar gêneros.')

    st.title('Remover Gênero')
    id = st.text_input('ID do Gênero')
    if st.button('Remover'):
        # É bom validar se o delete deu certo na sua service antes do success
        genre_service.delete_genre(id)
        st.success('Gênero removido com sucesso!')
        st.rerun()

    st.title('Atualizar Gênero')
    id = st.text_input('ID do Gênero', key='update_id')
    new_name = st.text_input('Novo Nome do Gênero', key='new_name')
    if st.button('Atualizar'):
        updated = genre_service.update_genre(id, new_name)
        if updated:
            st.success('Gênero atualizado com sucesso!')
            st.rerun()
        else:
            st.error('Erro ao atualizar gênero. Verifique se o gênero existe ou se você tem permissão para atualizar gêneros.')