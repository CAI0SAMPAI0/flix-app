# pyrefly: ignore [missing-import]
import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


actors = [
    {'id':1, 'name': 'Tom Hanks', 'nationality': 'American'},
    {'id':2, 'name': 'Meryl Streep', 'nationality': 'American'},
    {'id':3, 'name': 'Leonardo DiCaprio', 'nationality': 'American'},
    {'id':4, 'name': 'Kate Winslet', 'nationality': 'British'},
    {'id':5, 'name': 'Brad Pitt', 'nationality': 'American'}
]

actors_df = pd.DataFrame(actors)


def show_actors():
    st.title('Página de Atores/Atrizes')

    AgGrid(
        actors_df,
        editable=True,
        key='actors_grid',
    )

    st.title('Adicionar Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    nationality = st.text_input('Nacionalidade')
    if st.button('Adicionar'):
        actors.append({'id': len(actors) + 1, 'name': name, 'nationality': nationality})
        st.success('Ator/Atriz adicionado com sucesso!')
        st.rerun()

    st.title('Deletar Ator/Atriz')
    id = st.text_input('ID do Ator/Atriz')
    if st.button('Deletar'):
        actors.remove({'id': int(id)})
        st.success('Ator/Atriz deletado com sucesso!')
        st.rerun()

    st.title('Atualizar Ator/Atriz')
    new_name = st.text_input('Novo Nome do Ator/Atriz')
    new_nationality = st.text_input('Nova Nacionalidade')
    if st.button('Atualizar'):
        for actor in actors:
            if actor.get('id') == int(id):
                actor['name'] = new_name
                actor['nationality'] = new_nationality
                break
        st.success('Ator/Atriz atualizado com sucesso!')
        st.rerun()