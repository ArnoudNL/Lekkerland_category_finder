# Lekkerland Categoriekiezer

Een snelle en gebruiksvriendelijke webapplicatie om de juiste categorieën op te zoeken voor Lekkerland.

## Gebruik
De applicatie is live toegankelijk via de webbrowser (gehost op GitHub Pages). 

**Mobiel:** Je kunt de website openen op je telefoon (Safari/Chrome) en kiezen voor "Zet op beginscherm" om hem als een app te gebruiken.

## Lokale Ontwikkeling (Backend)
Dit project is gebouwd met een strikte Python-omgeving met `uv`, `FastAPI` en `pre-commit` controles.

Om de server lokaal te starten:
1. Installeer de packages: `uv pip install fastapi uvicorn`
2. Start de server: `uv run python main.py`
3. Open `http://localhost:8000` in je browser.