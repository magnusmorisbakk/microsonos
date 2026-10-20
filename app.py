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

# Links a slider to the update_volume function
st.slider(
    "Volume Level", 
    min_value=0, 
    max_value=100, 
    value=25, 
    step=1,
    key="volume_slider",
    on_change=update_volume
)