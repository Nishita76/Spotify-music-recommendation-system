# Spotify-music-recommendation-system
Welcome to the Spotify Music Recommendation System! This project demonstrates a music recommendation system built using a K-Nearest Neighbors (KNN) algorithm. The system is deployed using Flask for the backend API and Streamlit for the user interface. The model leverages a dataset of 30,000 songs with various features to recommend songs based on user input.

## Project Overview
The main goal of this project is to recommend songs based on an input song name. The project includes the following key components:

Data Preprocessing: Handling missing values, removing duplicates, and converting song names into numerical representations.
- Visualizing the distribution of various features to gain insights.
- Understanding the correlations between different audio features.

Model Training: Training a KNN model on the processed data to find similar songs.

API Development: Creating a Flask API to handle recommendation requests.

User Interface: Building a Streamlit app to provide a user-friendly interface for inputting song names and displaying recommendations.

## Deployment
Steps to test the app, run the following commands:
1. Clone the Repository, cd into the folder.
2. Install Dependencies
   '''
   pip install -r requirements.txt
   '''
4. Start the Flask Server
   python app.py
5. Start the Streamlit App
   In a new terminal, run:
   streamlit run streamlit_app.py
6. Test the Recommendation System
   - Select the song and click recommend
   

