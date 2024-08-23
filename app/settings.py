import os
import uuid
import rich
from rich.console import Console
from rich.text import Text
from pathlib import Path

console = Console()

def OutPutData(massage):
    console.print(massage, style="bold green")

def ErrorData(massage):
    console.print(massage, style="bold red")

BASE_DIR = Path(__file__).resolve().parent

DATA_BASE_URL = f"sqlite:///{BASE_DIR}/data/database.db"

IP_BANED = []

TEMPLATES_DIR = f"{BASE_DIR}/templates"

STAICS_DIR = f"{BASE_DIR}/static"
STAICS_ENDPOINT = "/static/"

MEDIA_DIR = f"{BASE_DIR}/media"
MEDIA_ENDPOINT = "/media/"