import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from GetPlaylists import *


client_credentials_manager = SpotifyClientCredentials(client_id='264a37295829463e9c1dceaa9562fa83', client_secret='f28f225f0ec74fad82fb2a5f8354ece6')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print (' ', i, t['name'])


result = sp.search(q='artist:' + '', type='artist')

try:
    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']

    related = sp.artist_related_artists(uri)
    print('Related artists for', name)
    for artist in related['artists']:
        print('  ', artist['name'])
except:
    print("usage show_related.py [artist-name]")


playlist = GetPlaylists()
playlist.print_playlists('spotify:user:22huxyo2nybfbc776hlw2ndbi')



