# spotify.py
import logging
import requests
from spotipy.oauth2 import SpotifyPKCE
from utils.config import SPOTIFY_CLIEND_ID, REDIRECT_UI, SPOTIFY_API, SPOTIFY_API_VERSION

auth = SpotifyPKCE(
    client_id=SPOTIFY_CLIEND_ID,
    redirect_uri=REDIRECT_UI,
    scope='streaming user-read-currently-playing',
    cache_path=".cache.spotify_auth",
)

def next_track():
    url = SPOTIFY_API+"/"+SPOTIFY_API_VERSION+"/me/player/next"

    try:
        access_token = auth.get_access_token()
        response = requests.post(url,
            headers={
                "Authorization": f"Bearer {access_token}"
            },
            timeout=10,
        )

        if 200 <= response.status_code < 300:
            return True

    except requests.RequestException as e:
        print(f"Error communicating with spotify: {e}")
        return False

def previous_track():
    url = SPOTIFY_API+"/"+SPOTIFY_API_VERSION+"/me/player/previous"
    
    try:
        access_token = auth.get_access_token()
        response = requests.post(url,
            headers={
                "Authorization": f"Bearer {access_token}"
            },
            timeout=10,
        )
    
        if 200 <= response.status_code < 300:
            return True
    
    except requests.RequestException as e:
        print(f"Error communicating with spotify: {e}")
        return False

def get_currently_playing():
    url = SPOTIFY_API+"/"+SPOTIFY_API_VERSION+"/me/player/currently-playing"

    try:
        access_token = auth.get_access_token()
        response = requests.get(url, 
                                headers= {
                                    "Authorization": f"Bearer {access_token}"
                                },
                                timeout=10,
                            )

        if response.status_code == 200:
            json_data = response.json()
            image_url = json_data["item"]["album"]["images"][0]["url"]

            return image_url
        
    except requests.RequestException as e:
        print(f"Error communicating with spotify: {e}")
        return False
        