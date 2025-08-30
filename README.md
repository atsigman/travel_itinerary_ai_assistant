# Travel Itinerary AI Assistant App
Web app providing example travel itineraries,
given a destination city, trip duration, and set of interests.

## Installation:
### Local/Virtual Environment:
Run `pip install -r requirements.txt`

### Docker:
A `Dockerfile` is included. Build the image via `docker build -t streamlit-app:latest .` or using `docker-compose`

## Groq API Key:
It will be necessary to create a Groq API key. This should be stored in a `.env` file in the project
root directory.  An `env_dummy.txt` file is provided with the appropriate keys as a reference. <br />

Groq: https://console.groq.com/keys <br />

## Running the App:
From the project root directory, execute: `streamlit run app.py`
(If targeting a specific python version, run `python3.x -m streamlit run app.py`)