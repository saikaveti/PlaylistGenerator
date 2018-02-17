import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

class GetPlaylists(object):
    def __init__(self):
        self.client_credentials_manager = SpotifyClientCredentials(client_id='264a37295829463e9c1dceaa9562fa83', client_secret='ce4945a01e554f9390459744f92a12b1')
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
    
    def print_playlists(self, username):
        token = util.prompt_for_user_token(username)

        if token:
            sp = spotipy.Spotify(auth=token)
            playlists = sp.user_playlists(username)
            for playlist in playlists['items']:
                print(playlist['name'])
        else:
            print("Can't get token for", username)