# app.py
import streamlit as st
import xml.etree.ElementTree as ET
   
from services.sonos_volume import post_retrieve_volume, post_set_volume
from services.sonos_music_controls import post_play_music, post_pause_music, post_next_track, post_previous_track
from services.sonos_currently_playing import get_sonos_playback_info

st.title("Sonos Controller Interface")

track_info = get_sonos_playback_info()

# ------ Playback Controls ------

def play_music():
    success = post_play_music()
    
    if success:
        st.toast("Music playback started.")
    else:
        st.error("Failed to start music playback.")

def pause_music():
    success = post_pause_music()
    
    if success:
        st.toast("Music playback paused.")
    else:
        st.error("Failed to pause music playback.")

def next_track():
    success = post_next_track()
    
    if success:
        st.toast("Skipped to the next track.")
    else:
        st.error("Failed to skip to the next track.")

def previous_track():
    success = post_previous_track()
    
    if success:
        st.toast("Went back to the previous track.")
    else:
        st.error("Failed to go back to the previous track.")

# ------ Volume Control ------

def update_volume():
    volume = st.session_state.volume_slider # Get the current value of the slider
    success = post_set_volume(volume) 
    
    if success:
        st.toast(f"Volume set to {volume}%") # Notify the user of volume change
    else:
        st.error("Failed to connect to the Sonos speaker.")


# ------ Playback Progress ------

def time_to_seconds(time_str):
    """Convert a time string in the format HH:MM:SS to total seconds."""
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


# ------ Currently Playing ------

@st.fragment(run_every=1)
def display_playback():
    track_info = get_sonos_playback_info()

    with st.container(border=True):
        if track_info:
            metadata = track_info['trackMetaData']

            if metadata:
                try:
                    root = ET.fromstring(metadata)

                    namespace = {'dc': 'http://purl.org/dc/elements/1.1/', 
                                'upnp': 'urn:schemas-upnp-org:metadata-1-0/upnp/'
                                 }
            
                    title = root.find('.//dc:title', namespace)
                    artist = root.find('.//dc:creator', namespace)
                    album = root.find('.//upnp:album', namespace)
                    album_art = root.find('.//upnp:albumArtURI', namespace)

                    col1, col2 = st.columns([1, 2])

                    with col1:
                        if album_art is not None and album_art.text:
                            album_art_url = album_art.text
                            st.image(album_art_url, width='content')

                    with col2:
                        st.markdown(title.text if title is not None else 'Unknown')
                        st.markdown(artist.text if artist is not None else 'Unknown')
                        st.markdown(album.text if album is not None else 'Unknown')

                    current_time = time_to_seconds(track_info["relTime"])
                    total_time = time_to_seconds(track_info["trackDuration"])

                    if total_time > 0:
                        progress = current_time / total_time

                        st.progress(min(progress, 1.0))

                        col1, col2 = st.columns([1, 0.1])

                        with col1:
                            st.caption(track_info["relTime"])

                        with col2:
                            st.caption(
                                track_info["trackDuration"])
                        
                    
                except ET.ParseError:
                    st.error("Failed to parse track metadata.")
            else:
                st.write("No metadata available for the current track.")

display_playback()

# ------ Playback Controls ------

with st.container(border=True):
    col_prev, col_play, col_pause, col_next = st.columns(4)

    with col_prev:
        col_prev.button(":previous_track_button:", on_click=previous_track, use_container_width=True)
    with col_play:
        col_play.button("▶", on_click=play_music, use_container_width=True)
    with col_pause:
        col_pause.button(":pause_button:", on_click=pause_music, use_container_width=True)
    with col_next:
        col_next.button(":next_track_button:", on_click=next_track, use_container_width=True)

st.slider ("Volume ", 
    min_value=0, 
    max_value=100, 
    value=post_retrieve_volume(), 
    step=1,
    key="volume_slider",
    on_change=update_volume)



