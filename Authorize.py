import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


username = sys.argv[1]

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(".cache-22huxyo2nybfbc776hlw2ndb")
    token = util.prompt_for_user_token(username)

spotifyObject = spotipy.Spotify(auth=token)

if token:
    spotifyObject.trace = False
    results = spotifyObject.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        print("%d %s" %(i, item['name']))
else:
    print("Can't get token for", username)




