import pickle
from sklearn.feature_extraction import image
import streamlit as st
import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import base64

st.set_page_config(page_title="Movies Recommender", layout='wide')
st.title('Movies Recommendation System')

df = pd.read_csv('main_data.csv')
cv = CountVectorizer(stop_words='english')
vector = cv.fit_transform(df['comb'])

similarity = cosine_similarity(vector)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=22eb0026986397f50a2bbd92a1c791b9&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['movie_title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:

        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].movie_title)

    return recommended_movie_names, recommended_movie_posters


def add_bg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg('image.jpg')

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = similarity

movie_list = movies['movie_title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0],
                 width=250, use_column_width='never')

    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1],
                 width=250, use_column_width='never')

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2],
                 width=250, use_column_width='never')

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3],
                 width=250, use_column_width='never')

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4],
                 width=250, use_column_width='never')

    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5],
                 width=250, use_column_width='never')

    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6],
                 width=250, use_column_width='never')

    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7],
                 width=250, use_column_width='never')

    with col9:
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8],
                 width=250, use_column_width='never')

    with col10:
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9],
                 width=250, use_column_width='never')
