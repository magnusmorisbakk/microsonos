# app.py
import streamlit as st
from services.sonos import retrieve_volume
import requests

API_ENDPOINT = "http://localhost:8000"

st.title("Sonos Controller Interface")

def retrieve_volume():
    try:
        res = requests.get(f"{API_ENDPOINT}/volume", timeout=4)
        if res.status_code == 200:
            return res.json().get("volume", 0)
    except requests.RequestException:
        pass
    return 0

def update_volume():
    volume = st.session_state.volume_slider
    try:
        res = requests.post(f"{API_ENDPOINT}/volume", json={"volume": volume}, timeout=4)
        if res.status_code == 200:
            st.toast(f"Volume set to {volume}")
        else:
            st.error("Failed to connect to sonos speaker")
    except requests.RequestException:
        st.error("Failed to connect to sonos speaker")

def play_music():
    try:
        res = requests.post(f"{API_ENDPOINT}/play", timeout=4)
        if res.status_code == 200:
            st.toast("Started music playback")
        else:
            st.error("Failed to start music playback")
    except requests.RequestException:
        st.error("Failed to start music playback")

def pause_music():
    try:
        res = requests.post(f"{API_ENDPOINT}/pause", timeout=4)
        if res.status_code == 200:
            st.toast("Paused track")
        else:
            st.error("Failed to pause track")
    except requests.RequestException:
        st.error("Failed to pause track")    

def next_track():
    try:
        res = requests.post(f"{API_ENDPOINT}/next", timeout=4)
        if res.status_code == 200:
            st.toast("Skipped track")
        else:
            st.error("Failed to skip track")
    except requests.RequestException:
        st.error("Failed to skip track")   

def previous_track():
    try:
        res = requests.post(f"{API_ENDPOINT}/previous", timeout=4)
        if res.status_code == 200:
            st.toast("Previous track")
        else:
            st.error("Failed to go back to previous track")
    except requests.RequestException:
        st.error("Failed to skip track") 

# Links a slider to the update_volume function

st.slider ("Volume Level", 
    min_value=0, 
    max_value=100, 
    value=retrieve_volume(), 
    step=1,
    key="volume_slider",
    on_change=update_volume)


col1, col2, col3, col4 = st.columns(4) 
col1.button(":previous_track_button:", on_click=previous_track, use_container_width=True)
col2.button("▶", on_click=play_music, use_container_width=True)
col3.button(":pause_button:", on_click=pause_music, use_container_width=True)
col4.button(":next_track_button:", on_click=next_track, use_container_width=True)


