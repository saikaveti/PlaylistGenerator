import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


client_credentials_manager = SpotifyClientCredentials(client_id='264a37295829463e9c1dceaa9562fa83', client_secret='ce4945a01e554f9390459744f92a12b1')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print (' ', i, t['name'])

result = sp.search(q='artist:' + 'open mike eagle', type='artist')
try:
    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']

    related = sp.artist_related_artists(uri)
    print('Related artists for', name)
    for artist in related['artists']:
        print('  ', artist['name'])
except:
    print("usage show_related.py [artist-name]")



