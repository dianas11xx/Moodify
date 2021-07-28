from SpotifyAuthorization import Authorization
from random import sample
import requests.exceptions
import spotipy

def songPredictions():
    try:
        user, client = Authorization()
        top_songs = user.get_popular_songs()
        new_songs = user.get_newest_songs()
        prediction_songs = user.compare_audio_features(client=client, popular_songs=top_songs, new_songs=new_songs)

        if len(prediction_songs) == 0:
            return "NO SONGS"

        if len(prediction_songs) > 30:  # Show random 30 (average for Spotify playlist creators)
            prediction_songs = sample(prediction_songs, 30)


        tracks = {}
        for track in prediction_songs:
            tracks[track['name']] = track['artists'][0]['name']

        playlist_name = "Next Popular Songs"

        description = "Here are our predictions for the next popular songs! Generated by Moodipy, an app that uses sentiment analysis to create a playlist that matches someone's mood."
        playlist_id = user.create_playlist(playlist_name=playlist_name, description=description)

        user.add_to_playlist(playlist_id=playlist_id, playlist_tracks=prediction_songs)

        print("checkpoint 3")

        return prediction_songs

    except(spotipy.exceptions.SpotifyException, requests.exceptions.HTTPError, spotipy.oauth2.SpotifyOauthError):
        return None
