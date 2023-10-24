import streamlit as st
from PIL import Image
import pandas as pd
from PIL import Image
import pickle
import numpy as np
import sklearn
model = pickle.load(open("randomf_model.sav", 'rb'))
st.title('NBA SALARY PREDICTION APP')
st.sidebar.header('Player Information')
image = Image.open("pexels-markus-spiske-1752757.jpg")
st.image(image, width=350)
def user_input():
    rating = st.sidebar.slider('ratings')
    jersey = st.sidebar.number_input('jersey', 0, 100, 1)
    team = st.sidebar.slider('team',0, 30, 1)
    position = st.sidebar.slider('position', 0, 10, 1)
    country = st.sidebar.slider('country', 0, 30, 1)
    draft_year = st.sidebar.slider('draft year', 2000, 2020, 2000)
    draft_round = st.sidebar.slider('draft round',1, 10, 1)
    draft_peak = st.number_input('draft peak', 1, 30, 1)

    input_data = {
        'rating': rating,
        'jersey': jersey,
        'team': team,
        'position': position,
        'country': country,
        'draft_year': draft_year,
        'draft_round': draft_round,
        'draft_peak': draft_peak
    }
    data = pd.DataFrame(input_data, index=[0])
    return data
user_data = user_input()
st.write(user_data)
prediction = model.predict(user_data)
st.subheader('Predicted Salary')
st.subheader('$'+str(np.round(prediction[0], 2)))
