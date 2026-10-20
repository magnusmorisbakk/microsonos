# config.py
from dotenv import load_dotenv
import os

load_dotenv()

SPEAKER_IP = os.getenv("SPEAKER_IP")
X_SONOS_API_KEY = os.getenv("X-SONOS-API-KEY")
X_SONOS_TARGET_UDN = os.getenv("X-SONOS-TARGET-UDN")