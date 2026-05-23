from actors.repository import ActorsRepository
import streamlit as st


class ActorsService:

    def __init__(self):
        self.actors_repo = ActorsRepository()

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state['actors']
        actors = self.actors_repo.get_actors()
        st.session_state.actors = actors
        return actors

    def get_actors_name(self):
        if 'actors_name' in st.session_state:
            return st.session_state['actors_name']
        actors = self.get_actors()
        actors_name = [actor.get('name') for actor in actors]
        st.session_state.actors_name = actors_name
        return actors_name

    def create_actor(self, actor):
        actor = dict(name=actor)
        actors = self.actors_repo.create_actor(actor)
        st.session_state.actors.append(actors)
        st.session_state.actors_name.append(actors.get('name'))
        return actors

    def update_actor(self, id, actor):
        actor = dict(name=actor)
        actors = self.actors_repo.update_actor(id, actor)
        st.session_state.actors.append(actors)
        st.session_state.actors_name.append(actors.get('name'))
        return actors
        return self.actors_repo.update_actor(id, actor)

    def delete_actor(self, id):
        return self.actors_repo.delete_actor(id)