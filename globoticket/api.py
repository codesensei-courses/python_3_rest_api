"""
api.py
---

The REST Api for the Globoticket events database.
"""

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

PROJECT_ROOT = Path(__file__).parent.parent
app.mount("/", StaticFiles(directory=PROJECT_ROOT / "static", html=True))

