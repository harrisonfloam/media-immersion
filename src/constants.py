import os

from dotenv import load_dotenv

load_dotenv()

TMDB_API_TOKEN = os.getenv("TMDB_API_TOKEN")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3/"
TMDB_HEADERS = {"accept": "application/json", "Authorization": f"Bearer {TMDB_API_KEY}"}
