# THIS MODULE IS STILL IN THE TESTING PHASE
# Create a Playlist from Sentiment Analysis and Track Analysis
from Spotipy import User
import SpotifyAuthorization
from SpotifyAuthorization import client
from SpotifyAuthorization import user


""" 
Step 0: Get Users Liked Songs
"""
user_songs = user.get_user_saved_tracks() 
# Check that all songs are gotten
# for i, track in enumerate(user_songs, 1):
#     print(i, track['name'])


"""
Step 1: Get Tracks Matching User Emotion
"""
first_emotion = "sadness"
second_emotion = "awful"
emotion_tracks = user.get_user_emotion_tracks(client=client,user_tracks=user_songs, base_emotion=first_emotion, second_emotion=second_emotion)
# Check that all songs are gotten
# for i, track in enumerate(f_emotion_tracks, 1):
#     print(i, track['name'])

"""
Step 2: Create a Playlist for the User
"""
playlist_name = first_emotion
description = "This is a new playlist!"
user.create_playlist(playlist_name=playlist_name, description=description)

"""
Step 3: Add Songs to a Playlist
"""
user.add_to_playlist(playlist_name=playlist_name, playlist_tracks=emotion_tracks)