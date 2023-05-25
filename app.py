import streamlit as st
import pickle 
import pandas as pd 


# Importing Databases
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommended(selected_movie_name):
    movies_index = movies[movies['title'] == selected_movie_name ].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)) , reverse=True , key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    
    for i in movies_list :
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies







from PIL import Image

image = Image.open('Movies-on-the-House.jpg')

st.title('Movie Recommender System')


st.image(image , caption='Made with ❤️ by Shantanu Nimkar')


selected_movie_name = st.selectbox(
    'Search Here !' ,
    movies['title'].values
)


if st.button('Recommended Movie'):
    recommendations = recommended(selected_movie_name)
    for i in recommendations:
        st.write(i)


