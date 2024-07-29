# Movie Recommender System

Dataset Link:-https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGE3Z0RIM3l2bHBmMkNNRmVLMDJrQlZLVFFRUXxBQ3Jtc0tuR044S3RlZFhBbnM1MGczRDFzRjBfbnFKVTBNR0hBNnpiaWZKYVVFcUJNZWZkeFc4QWY1VjA4Ymw2eHJ2Z3pKYkVQSEpUUHpkZ0hCWkttdDBDX29sVUozSVB1OXdyLUhTNnZQVEFEN2hRRS1feUkzbw&q=https%3A%2F%2Fwww.kaggle.com%2Ftmdb%2Ftmdb-movie-metadata%3Fselect%3Dtmdb_5000_movies.csv&v=1xtrIEwY_zY

This project involves building a movie recommender system using movie metadata. The system uses natural language processing techniques to recommend similar movies based on user input.

## Key Features

- **Data Preparation**: Loads and processes movie and credit data, including handling missing values and converting text data into numerical vectors.
- **Feature Engineering**: Uses text vectorization and stemming to prepare data for similarity analysis.
- **Similarity Calculation**: Computes cosine similarity between movies to determine how similar they are to each other.
- **Recommendation System**: Provides recommendations for movies similar to a user-selected movie.
- **Web Application**: Implements a web-based user interface using Streamlit for movie recommendations and poster display.

## Requirements

- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- NLTK
- Streamlit
- Requests

## Setup

1. **Install Dependencies**

   Ensure you have the necessary Python packages installed. You can install them using pip:

   ```bash
   pip install numpy pandas scikit-learn nltk streamlit requests
Download Data

Place the movie dataset and credits dataset in the specified directory. Update the paths in the script if necessary:

tmdb_5000_movies.csv
tmdb_5000_credits.csv
Run the Recommender System

To train the model and save the necessary data, run the script. Ensure you have the movies_dict.pkl and similarity.pkl files available for the Streamlit app.

bash
Copy code
python Recommender_system.py
Start the Streamlit App

Launch the Streamlit app to use the recommender system:

bash
Copy code
streamlit run app.py
Code Overview
1. Data Preparation
Loading Data: Loads movie and credits data from CSV files.
Merging Data: Combines movie data with credits.
Feature Selection: Selects relevant columns and handles missing values.
Text Processing: Converts text data (genres, keywords, cast, crew) into a format suitable for vectorization.
2. Text Vectorization and Stemming
Vectorization: Uses CountVectorizer to convert text tags into numerical vectors.
Stemming: Applies stemming to reduce words to their root form, improving similarity calculations.
3. Similarity Calculation
Cosine Similarity: Computes similarity between movies based on vectorized tags.
Recommendation Function: Finds and returns the top 5 most similar movies to a given movie.
4. Web Application
Streamlit Integration: Provides an interactive interface where users can select a movie and receive recommendations along with movie posters.
Fetch Movie Posters: Uses the TMDb API to retrieve and display movie posters.
Example
The following example demonstrates how to use the recommender system:

python
Copy code
import pandas as pd
import pickle

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movie_list:
        print(movies.iloc[i[0]].title)

recommend('Batman Begins')
License
This project is licensed under the MIT License - see the LICENSE file for details.
