# Import necessary libraries
import pickle
from flask import Flask, request, jsonify
import pandas as pd

# Load the saved model and vectorizer
knn_model = pickle.load(open("D:\music data\knn_model.pkl", 'rb'))

cvectorizer = pickle.load(open("D:\music data\cvectorizer.pkl", 'rb'))

# Load the dataset
df = pd.read_pickle("D:\music data\df.pkl")

# Create a set of song names for quick lookup
song_names_set = set(df['track_name'])

# Initialize Flask app
app = Flask(__name__)

# Define recommendation function
def recommend_song(input_song_name, num_recommendations=5):
    input_song_vec = cvectorizer.transform([input_song_name])
    distances, indices = knn_model.kneighbors(input_song_vec)
    recommended_songs = [df['track_name'].iloc[idx] for idx in indices.flatten()]
    return recommended_songs


@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    input_song_name = data['song_name']
    song_names_set = set(df['track_name'])
    print(f"Received request for song: {input_song_name}")

    if input_song_name not in song_names_set:
        return jsonify({"Song not found. Please try again with a different song name."})

    # Transform input song name
    input_song_vec = cvectorizer.transform([input_song_name])
    
    # Find nearest neighbors
    distances, indices = knn_model.kneighbors(input_song_vec)
    
    # Get recommended songs
    recommended_songs = [df['track_name'].iloc[idx] for idx in indices.flatten()]
    
    print(f"Recommended songs: {recommended_songs}")
    
    return jsonify(recommended_songs)

if __name__ == '__main__':
    app.run(debug=True)

