# sonos.py
import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()
SPEAKER_IP = os.getenv("SPEAKER_IP")
X_SONOS_API_KEY = os.getenv("X-SONOS-API-KEY")
X_SONOS_TARGET_UDN = os.getenv("X-SONOS-TARGET-UDN")

def set_volume_level(volume_level: int) -> bool:
    """Sets the volume on the Sonos speaker. Returns True if successful."""
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
    except requests.RequestException as e:
        print(f"Error communicating with Sonos: {e}")
        return False