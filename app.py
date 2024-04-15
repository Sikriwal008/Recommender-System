import pandas as pd
import streamlit as st
import pickle
import requests  # For making requests to an API for movie posters


# Function to fetch the movie poster given a movie ID
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    print(data)
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# Function to recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # Fetching the row number of that movie
    distance = similarity[movie_index]
    # Sort movies based on similarity and take the top 5 (excluding the selected movie)
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    movie_name = []
    movie_poster = []
    # Fetch names and posters of recommended movies
    for i in movie_list:
        movie_name.append(movies.iloc[i[0]].title)
        movie_id = movies.iloc[i[0]].id
        movie_poster.append(fetch_poster(movie_id))
    return movie_name, movie_poster


# Load movie data and similarity matrix from pickle files
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app title
st.title('Movie Recommender System')

# Select box to choose a movie
select_movie_name = st.selectbox('Enter movie name:', (movies['title'].values))

# Button to trigger recommendation
if st.button('Recommend'):
    # Call recommend function to get recommended movie names and posters
    recommended_movie_names, recommended_movie_posters = recommend(select_movie_name)

    for i in range(0,5):
        st.text(recommended_movie_names[i])
        st.image(recommended_movie_posters[i])

