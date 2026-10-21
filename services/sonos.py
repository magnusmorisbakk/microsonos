# sonos.py
# from urllib import response
import uuid
import requests
from utils.config import SPEAKER_IP, X_SONOS_API_KEY, X_SONOS_TARGET_UDN
import xml.etree.ElementTree as ET

def retrieve_volume():
    """Sets the volume on the Sonos speaker. Returns True if successful."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/RenderingControl/Control"
        
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:RenderingControl:1#GetVolume"',
        "X-Sonos-Api-Key": X_SONOS_API_KEY,
        "X-Sonos-Corr-Id": str(uuid.uuid4()),
        "X-SONOS-TARGET-UDN": X_SONOS_TARGET_UDN
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

def play_music():
    """Sends a command to the Sonos speaker to start playing music."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#Play"',
        "X-Sonos-Api-Key": X_SONOS_API_KEY,
        "X-Sonos-Corr-Id": str(uuid.uuid4()),
        "X-SONOS-TARGET-UDN": X_SONOS_TARGET_UDN
    }
    
    body = f"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <s:Body>
        <u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
            <InstanceID>0</InstanceID>
            <Speed>1</Speed>
        </u:Play>
    </s:Body>
</s:Envelope>"""

    try:
        response = requests.post(url, headers=headers, data=body, timeout=3)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error communicating with Sonos: {e}")
        return False

def pause_music():
    """Sends a command to the Sonos speaker to pause music playback."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#Pause"',
        "X-Sonos-Api-Key": X_SONOS_API_KEY,
        "X-Sonos-Corr-Id": str(uuid.uuid4()),
        "X-SONOS-TARGET-UDN": X_SONOS_TARGET_UDN
    }
    
    body = f"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <s:Body>
        <u:Pause xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
            <InstanceID>0</InstanceID>
        </u:Pause>
    </s:Body>
</s:Envelope>"""

    try:
        response = requests.post(url, headers=headers, data=body, timeout=3)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error communicating with Sonos: {e}")
        return False    

def next_track():
    """Sends a command to the Sonos speaker to skip to the next track."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#Next"',
        "X-Sonos-Api-Key": X_SONOS_API_KEY,
        "X-Sonos-Corr-Id": str(uuid.uuid4()),
        "X-SONOS-TARGET-UDN": X_SONOS_TARGET_UDN
    }
    
    body = f"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <s:Body>
        <u:Next xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
            <InstanceID>0</InstanceID>
        </u:Next>
    </s:Body>
</s:Envelope>"""

    try:
        response = requests.post(url, headers=headers, data=body, timeout=3)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error communicating with Sonos: {e}")
        return False 

def previous_track():
    """Sends a command to the Sonos speaker to go back to the previous track."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#Previous"',
        "X-Sonos-Api-Key": X_SONOS_API_KEY,
        "X-Sonos-Corr-Id": str(uuid.uuid4()),
        "X-SONOS-TARGET-UDN": X_SONOS_TARGET_UDN
    }
    
    body = f"""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <s:Body>
        <u:Previous xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
            <InstanceID>0</InstanceID>
        </u:Previous>
    </s:Body>
</s:Envelope>"""

    try:
        response = requests.post(url, headers=headers, data=body, timeout=3)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error communicating with Sonos: {e}")
        return False
    