# volume.py
import requests
import uuid
import os
from dotenv import load_dotenv

load_dotenv()
SPEAKER_IP = os.getenv("SPEAKER_IP")
X_SONOS_API_KEY = os.getenv("X-SONOS-API-KEY")
X_SONOS_TARGET_UDN = os.getenv("X-SONOS-TARGET-UDN")

def handle_volume_adjustment():
    while True:
        action = input("\nSet volume level (0-100) or [B] to go back: ")

        if action.upper() == "B":
            break
        elif action.isdigit() and 0 <= int(action) <= 100:
            volume_level = int(action)
            set_volume_level(volume_level)

def set_volume_level(volume_level):
    print(f"\nSetting volume to {volume_level} on the Sonos speaker.")
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/RenderingControl/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:RenderingControl:1#SetVolume"',
        "X-Sonos-Api-Key": X_SONOS_API_KEY,
        "X-Sonos-Corr-Id": str(uuid.uuid4()),
        "X-SONOS-TARGET-UDN": X_SONOS_TARGET_UDN
    }
    
    body = f"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <s:Body>
        <u:SetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1">
            <InstanceID>0</InstanceID>
            <Channel>Master</Channel>
            <DesiredVolume>{volume_level}</DesiredVolume>
        </u:SetVolume>
    </s:Body>
</s:Envelope>"""
    try:
        response = requests.post(url, headers=headers, data=body, timeout=3)
        return response.status_code == 200
    except requests.RequestException:
        return False