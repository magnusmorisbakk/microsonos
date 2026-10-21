# main.py
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from services.sonos import retrieve_volume, set_volume_level, play_music, pause_music, next_track, previous_track

app = FastAPI()

class VolumeRequest(BaseModel):
    volume: int

@app.get("/volume")
def get_volume():
    volume = retrieve_volume()
    if volume is False or volume is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve volume from Sonos speaker")
    return{"volume": volume}

@app.post("/volume", response_model=None)
def set_volume(payload: VolumeRequest):
    success = set_volume_level(payload.volume)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to set volume")
    return{"status": "success"}

@app.post("/play", response_model=None)
def play():
    if not play_music():
        raise HTTPException(status_code=500, detail="Failed to start music")
    return {"status": "success"}

@app.post("/pause", response_model=None)
def pause():
    if not pause_music():
        raise HTTPException(status_code=500, detail="Failed to pause music")
    return {"status": "success"}

@app.post("/next", response_model=None)
def next():
    if not next_track():
        raise HTTPException(status_code=500, detail="Failed to go to next track")

@app.post("/previous", response_model=None)
def previous():
    if not previous():
        raise HTTPException(status_code=500, detail="Failed to go to previous track")
    return {"status": "success"}


