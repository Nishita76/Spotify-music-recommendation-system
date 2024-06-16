import streamlit as st
import requests
import pandas as pd

# Load the dataset
df = pd.read_pickle("D:\music data\df.pkl")

st.title("Spotify Music Recommendation System")

# Create a dropdown menu for song selection
song_list = df['track_name'].tolist()
input_song_name = st.selectbox("Select a song:", song_list)

# Input song name
#input_song_name = st.text_input("Enter a song name:")()

# When the button is clicked
if st.button("Recommend"):
    
    try:
        response = requests.post('http://localhost:5000/recommend', json={'song_name': input_song_name})
    
    # Display recommendations
        if response.status_code == 200:
            recommendations = response.json()
            st.write("Recommended Songs:")
            for i, song in enumerate(recommendations):
                st.write(f"{i+1}. {song}")

        else:
            st.write("Error: Could not retrieve recommendations.")
            st.write(f"Status Code: {response.status_code}")
            st.write(f"Response: {response.text}")
    except Exception as e:
        st.write(f"Error: {e}")

#run streamlit run streamlit_app.py

