

import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Connect to .env
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Connect to Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = Spotify(auth_manager=auth_manager)

# Choose Funkadelic as artist through id
artist_id = 'spotify:artist:450o9jw6AtiQlQkHCdH6Ru'

# Get top 10 tracks with .artist_top_track built-in funtion
tracks = sp.artist_top_tracks(artist_id)

# Covert .json in DataFrame
df = pd.json_normalize(tracks['tracks'])

# Create duration in minutes column
df['duration_m'] = (df['duration_ms'] / 60000).round(2)

# Create a DataFrame for the top 3 tracks
top3 = df.sort_values("popularity", ascending = False).head(3)

# Plot the relation of popularity with diration
sns.scatterplot(data = top3, x = "duration_m", y = "popularity", hue = "name")

plt.xlabel('Duration')
plt.ylabel('Popularity')
plt.legend()
plt.savefig("/workspaces/interacting-with-api-python-project-tutorial/image/Funkadelic_Top3_DP-relation.png")
