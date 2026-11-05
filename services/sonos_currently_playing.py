import xml.etree.ElementTree as ET
import requests
from utils.config import SPEAKER_IP

def get_sonos_playback_info():
    """Retrieves the currently playing track information from the Sonos speaker."""
    url = f"http://{SPEAKER_IP}:1400/MediaRenderer/AVTransport/Control"
    
    headers = {
        "Content-Type": 'text/xml; charset="utf-8"',
        "SOAPACTION": '"urn:schemas-upnp-org:service:AVTransport:1#GetPositionInfo"',
    }
    
    body = """<?xml version="1.0" encoding="utf-8"?>
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
        <s:Body>
            <u:GetPositionInfo xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
                <InstanceID>0</InstanceID>
            </u:GetPositionInfo>
        </s:Body>
    </s:Envelope>"""

    try:
        response = requests.post(url, headers=headers, data=body, timeout=3)
        if response.status_code == 200:
            root = ET.fromstring(response.content)

            track = root.find('.//{*}Track')
            track_duration = root.find('.//{*}TrackDuration')
            track_metadata = root.find('.//{*}TrackMetaData')
            rel_time = root.find('.//{*}RelTime')
            abs_time = root.find('.//{*}AbsTime')

            track_info = {
                "track": track.text if track is not None else None,
                "trackDuration": track_duration.text if track_duration is not None else None,
                "trackMetaData": track_metadata.text if track_metadata is not None else None,
                "relTime": rel_time.text if rel_time is not None else None,
                "absTime": abs_time.text if abs_time is not None else None,
            }
            
            return track_info
        else:
            print(f"Failed to retrieve playback info. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error occurred while fetching playback info: {e}")
        return None