# sonos.py
import requests
from utils.config import SPEAKER_IP
    

def post_play_music():
    """Sends a command to the Sonos speaker to start playing music."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#Play"',
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

def post_pause_music():
    """Sends a command to the Sonos speaker to pause music playback."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#Pause"',
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

def post_next_track():
    """Sends a command to the Sonos speaker to skip to the next track."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#Next"',
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

def post_previous_track():
    """Sends a command to the Sonos speaker to go back to the previous track."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#Previous"',
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
    