import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import os
import spotipy

class GetPlaylists(object):
    def __init__(self):
        self.CLIENT_ID = '264a37295829463e9c1dceaa9562fa83'
        self.CLIENT_SECRET = 'f28f225f0ec74fad82fb2a5f8354ece6'
        self.REDIRECT = 'https://www.google.com/'
        self.client_credentials_manager = SpotifyClientCredentials(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
    
    def print_playlists(self, username):

        try:
            token = util.prompt_for_user_token(username)
        except:
            os.remove(".cache-22huxyo2nybfbc776hlw2ndb")
            token = util.prompt_for_user_token(username)

        spotifyObject = spotipy.Spotify(auth=token)

        if token:
            playlists = spotifyObject.user_playlists(username)
            for playlist in playlists['items']:
                print(playlist['name'])
        else:
            print("Can't get token for", username)