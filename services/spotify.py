# spotify.py
import requests
from spotipy.oauth2 import SpotifyPKCE
from utils.config import SPOTIFY_CLIEND_ID, REDIRECT_UI, SPOTIFY_API, SPOTIFY_API_VERSION

auth = SpotifyPKCE(
    client_id=SPOTIFY_CLIEND_ID,
    redirect_uri=REDIRECT_UI,
    scope='streaming',
    cache_path=".cache.spotify_auth",
)

def next_track():
    access_token = auth.get_access_token()
    url = SPOTIFY_API+"/"+SPOTIFY_API_VERSION+"/me/player/next"

    try:
        response = requests.post(url,
            headers={
                "Authorization": f"Bearer {access_token}"
            },
            timeout=10,
        )

        if response.status_code == 204:
            return True

    except requests.RequestException as e:
        print(f"Error communicating with spotify: {e}")
        return False

def previous_track():
    access_token = auth.get_access_token()
    url = SPOTIFY_API+"/"+SPOTIFY_API_VERSION+"/me/player/previous"
    
    try:
        response = requests.post(url,
            headers={
                "Authorization": f"Bearer {access_token}"
            },
            timeout=10,
        )
    
        if response.status_code == 204:
            return True
    
    except requests.RequestException as e:
        print(f"Error communicating with spotify: {e}")
        return False
    