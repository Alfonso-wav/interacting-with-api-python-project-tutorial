# Import libraries
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Connect to .env
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Connect to Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Choose Funkadelic as the artist using their ID
artist_id = 'spotify:artist:450o9jw6AtiQlQkHCdH6Ru'

# Get the top 10 tracks using the artist_top_tracks built-in function
tracks = sp.artist_top_tracks(artist_id)

# Convert the JSON data to a DataFrame
df = pd.json_normalize(tracks['tracks'])

# Create a duration in minutes column
df['duration_m'] = (df['duration_ms'] / 60000).round(2)

# Create a DataFrame for the top 3 tracks
top3 = df.sort_values("popularity", ascending=False).head(3)

# Plot the relationship between popularity and duration
sns.scatterplot(data=top3, x="duration_m", y="popularity", hue="name")

plt.xlabel('Duration')
plt.ylabel('Popularity')
plt.legend()

plt.show()