"""Client methods for interacting with the TMDB API."""

import os

import requests
from dotenv import load_dotenv

from src.constants import BASE_URL, TMDB_HEADERS

load_dotenv()


def fetch_movies(filters: dict, page: int = 1) -> dict:
    """
    Retrieve movies from TMDb discover endpoint using provided filters.

    https://developer.themoviedb.org/reference/discover-movie

    :param filters: Dictionary containing TMDb query parameters.
    :param page: The page number for pagination (default is 1).
    :return: Parsed JSON response as a dictionary.
    """
    # TODO: abstract pagination, just return list of movies
    url = BASE_URL + "discover/movie"
    params = {"page": page}
    params.update(filters)

    response = requests.get(url, headers=TMDB_HEADERS, params=params)
    response.raise_for_status()
    return response.json()
