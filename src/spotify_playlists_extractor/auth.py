"""This module contains the functions to authenticate with the Spotify API."""

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from .settings import get_settings


def get_spotify_client(scope: str = "playlist-read-private") -> spotipy.Spotify:
    """Get a Spotify client with the given scope.

    Returns:
        spotipy.Spotify: A Spotify client.
    """
    settings = get_settings()
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=settings.SPOTIFY_CLIENT_ID,
            client_secret=settings.SPOTIFY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIFY_REDIRECT_URI,
            scope=scope,
        )
    )
    return sp
