# microsonos
Lightweight local controller for Sonos speakers reverse enginnered from UPnP/SOAP network traffic.

---
## Featues
* Volume Control
* Playback Control
* Current Volume Retrieval
* .env based config

---
## Tech Stack

* Python
* Streamlit
* Sonos API Integration

---
## Project Structure
```
microsonos/
├─ app.py
├─ utils/
│  └─ config.py    
├─ services    
│  └─ sonos.py 
├─ .env
└─ .gitignore
```
---
## Requirements
* Python
* A Sonos speaker accessible from the client running the application
* The required API access and config for Sonos integration

---
## Installation
### Clone Repository
```bash
git clone https://github.com/magnusmorisbakk/microsonos.git
cd microsonos
```
### Create virtual environment
```bash
python -m venv .venv
```
Activate environment:

**PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

### Install dependencies
```bash
pip install streamlit python-dotenv
```

### Configure env variables
```
SPEAKER_IP=your_sonos_speaker_ip
X-SONOS-API-KEY=your_sonos_api_key
X-SONOS-TARGET-UDN=your_sonos_udn
```

### Start the application
```bash
strealit run app.py
```
The streamlit based web application will be accessible through a local url displayed in the terminal.

