
YOUR_UNIQUE_CLIENT_ID = "9388a966cd004c87aadec4140353729c"
YOUR_UNIQUE_CLIENT_SECRECT = "1251e35338364da7aceacea91ce94655"

REDIRECT_URI = "https://www.billboard.com/charts/hot-100/"
import streamlit as st
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import re

st.title("Billboard Top 100 Playlist Creator")

# User input for date
date = st.text_input("Enter a date (YYYY-MM-DD):")

if st.button("Create Playlist"):
    # Validate date format
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        st.error("Invalid date format! Please enter in YYYY-MM-DD format.")
    else:
        # Scrape Billboard Hot 100
        billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url=billboard_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        song_names_spans = soup.select("li ul li h3")
        song_names = [song.getText().strip() for song in song_names_spans]

        if not song_names:
            st.error("No songs found for this date. Please try another date.")
        else:
            st.success(f"Found {len(song_names)} songs!")

            # Spotify Authentication
            sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri=REDIRECT_URI,
                client_id=YOUR_UNIQUE_CLIENT_ID,
                client_secret=YOUR_UNIQUE_CLIENT_SECRECT,
                show_dialog=True,
                cache_path="token.txt"
            ))
            user_id = sp.current_user()["id"]

            # Search Spotify for songs
            song_uris = []
            year = date.split("-")[0]
            for song in song_names:
                result = sp.search(q=f"track:{song} year:{year}", type="track")
                try:
                    uri = result["tracks"]["items"][0]["uri"]
                    song_uris.append(uri)
                except IndexError:
                    st.warning(f"{song} not found on Spotify. Skipped.")

            # Create a Spotify playlist
            playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100 - {date}", public=False)
            sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
            st.success(f"Playlist Created! [Open in Spotify](https://open.spotify.com/playlist/{playlist['id']})")

            # Save song list for download
            df = pd.DataFrame({"Song": song_names})
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Playlist as CSV", data=csv, file_name="playlist.csv", mime="text/csv")
