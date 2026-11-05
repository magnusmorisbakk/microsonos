# sonos_volume.py
import requests
from utils.config import SPEAKER_IP
import xml.etree.ElementTree as ET


def post_retrieve_volume():
    """Retrieves the current volume level from the Sonos speaker. Returns the volume level if successful, otherwise False."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/RenderingControl/Control"
        
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:RenderingControl:1#GetVolume"',
        }
        
    body = f"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <s:Body>
    <u:GetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1">
        <InstanceID>0</InstanceID>
        <Channel>Master</Channel>
    </u:GetVolume>
    </s:Body>
</s:Envelope>"""
    
    try:
        response = requests.post(url, headers=headers, data=body, timeout=3)

        if response.status_code == 200:
            root = ET.fromstring(response.text)
            volumeId = root.find('.//CurrentVolume')

            if volumeId is not None and volumeId.text is not None:
                currentVolume = int(volumeId.text)
                return currentVolume

    except requests.RequestException as e:
        print(f"Error communicating with Sonos: {e}")
        return False

def post_set_volume(volume_level: int) -> bool:
    """Sets the volume on the Sonos speaker. Returns True if successful."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/RenderingControl/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:RenderingControl:1#SetVolume"',
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

    
    