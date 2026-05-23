# pyrefly: ignore [missing-import]
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


reviews = [
    {'id':1, 'title': 'Titanic', 'rating': 4},
    {'id':2, 'title': 'The Lion King', 'rating': 5},
    {'id':3, 'title': 'The Matrix', 'rating': 4},
    {'id':4, 'title': 'The Godfather', 'rating': 5},
    {'id':5, 'title': 'The Dark Knight', 'rating': 4}
]

reviews_df = pd.DataFrame(reviews)


def show_reviews():
    st.title('Página de Avaliações')

    AgGrid(
        reviews_df,
        editable=True,
        key='reviews_grid',
    )

    st.title('Adicionar review')
    title = st.text_input('Título')
    rating = st.text_input('Avaliação')
    if st.button('Adicionar'):
        reviews.append({'id': len(reviews) + 1, 'title': title, 'rating': rating})
        st.success('Review adicionado com sucesso!')
        st.rerun()

    st.title('Deletar Review')
    id = st.text_input('ID do Review')
    if st.button('Deletar'):
        reviews.remove({'id': int(id)})
        st.success('Review deletado com sucesso!')
        st.rerun()

    st.title('Atualizar Review')
    title = st.text_input('Novo Título do Review')
    rating = st.text_input('Nova Avaliação')
    if st.button('Atualizar'):
        for review in reviews:
            if review.get('id') == int(id):
                review['title'] = title
                review['rating'] = rating
                break
        st.success('Review atualizado com sucesso!')
        st.rerun()