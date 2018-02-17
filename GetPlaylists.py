import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class GetPlaylists(object):
    def __init__(self):
        self.client_credentials_manager = SpotifyClientCredentials(client_id='264a37295829463e9c1dceaa9562fa83',                                                   client_secret='ce4945a01e554f9390459744f92a12b1')
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
    
