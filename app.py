import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_pic(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0dc5098615a252c4f34bc13868c9bef6&language=en-US'.format(movie_id))
    data= response.json()

    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie):
    movie_index = movies[movies['title'] == movie] .index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended = []
    recommended_movie_poster = []
    for i in movies_list:
        movie_id= movies.iloc[i[0]].movie_id

        recommended.append(movies.iloc[i[0]].title)
        # fetch movie poster
        recommended_movie_poster.append(fetch_pic(movie_id))
    return recommended,recommended_movie_poster

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title("Movie Recommender System")
select_movie_name = st.selectbox(
     'How would you like to be contacted?', movies['title'].values)




if st.button('Search'):
    names, poster = recommend(select_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])

