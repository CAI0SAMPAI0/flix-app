from reviews.repository import ReviewRepository
import streamlit as st


class ReviewService:

    def __init__(self):
        self.review_repo = ReviewRepository()

    def get_reviews(self):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews = self.review_repo.get_reviews()
        st.session_state.reviews = reviews
        return reviews

    def get_reviews_name(self):
        if 'reviews_name' in st.session_state:
            return st.session_state.reviews_name
        reviews = self.get_reviews()
        reviews_name = [review.get('title') for review in reviews]
        st.session_state.reviews_name = reviews_name
        return reviews_name

    def create_review(self, review):
        review = dict(title=review.get('title'),
                      rating=review.get('rating'))
        reviews = self.review_repo.create_review(review)
        st.session_state.reviews.append(reviews)
        st.session_state.reviews_name.append(reviews.get('title'))
        return reviews

    def update_review(self, id, review):
        review = dict(title=review.get('title'),
                      rating=review.get('rating'))
        reviews = self.review_repo.update_review(id, review)
        st.session_state.reviews.append(reviews)
        st.session_state.reviews_name.append(reviews.get('title'))
        return reviews

    def delete_review(self, id):
        return self.review_repo.delete_review(id)