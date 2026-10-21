# spotify.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from utils.config import SPOTIFY_CLIEND_ID, SPOTIFY_CLIENT_SECRET, REDIRECT_UI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIEND_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=REDIRECT_UI,
                                               scope='streaming',
                                               show_dialog=True))

def next_track(self, device_id=SPOTIFY_CLIEND_ID):
    return self._post(self._append_device_id("me/player/next", device_id))