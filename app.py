# app.py
import streamlit as st
from services.sonos import set_volume_level

st.title("Sonos Controller Interface")

def update_volume():
    volume = st.session_state.volume_slider # Get the current value of the slider
    success = set_volume_level(volume) 
    
    if success:
        st.toast(f"Volume set to {volume}%") # Notify the user of volume change
    else:
        st.error("Failed to connect to the Sonos speaker.")

def play_music():
    from services.sonos import play_music
    success = play_music()
    
    if success:
        st.toast("Music playback started.")
    else:
        st.error("Failed to start music playback.")

def pause_music():
    from services.sonos import pause_music
    success = pause_music()
    
    if success:
        st.toast("Music playback paused.")
    else:
        st.error("Failed to pause music playback.")

def next_track():
    from services.sonos import next_track
    success = next_track()
    
    if success:
        st.toast("Skipped to the next track.")
    else:
        st.error("Failed to skip to the next track.")

def previous_track():
    from services.sonos import previous_track
    success = previous_track()
    
    if success:
        st.toast("Went back to the previous track.")
    else:
        st.error("Failed to go back to the previous track.")

# Links a slider to the update_volume function

st.slider ("Volume Level", 
    min_value=0, 
    max_value=100, 
    value=25, 
    step=1,
    key="volume_slider",
    on_change=update_volume)


col1, col2, col3, col4 = st.columns(4) 
col1.button(":previous_track_button:", on_click=previous_track, use_container_width=True)
col2.button("▶", on_click=play_music, use_container_width=True)
col3.button(":pause_button:", on_click=pause_music, use_container_width=True)
col4.button(":next_track_button:", on_click=next_track, use_container_width=True)


