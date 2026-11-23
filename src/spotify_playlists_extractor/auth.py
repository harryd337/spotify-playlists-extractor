"""This module contains the functions to authenticate with the Spotify API."""

import spotipy
from requests import Session
from requests.adapters import HTTPAdapter
from spotipy.oauth2 import SpotifyOAuth
from urllib3.util.retry import Retry

from .settings import get_settings

DEFAULT_REQUEST_TIMEOUT = 30
DEFAULT_RETRIES = 3


def _build_session(retries: int = DEFAULT_RETRIES) -> Session:
    """Build a requests session that retries transient network failures.

    Unlike spotipy's default session, this enables retries on read timeouts so
    that a single slow response does not abort a long extraction run.

    Args:
        retries (int): The number of times to retry a failed request.

    Returns:
        Session: A requests session with retry behaviour configured.
    """
    retry = Retry(
        total=retries,
        connect=retries,
        read=retries,
        status=retries,
        backoff_factor=0.3,
        allowed_methods=frozenset(["GET", "POST", "PUT", "DELETE"]),
        status_forcelist=spotipy.Spotify.default_retry_codes,
    )
    session = Session()
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def get_spotify_client(
    scope: str = "playlist-read-private",
    requests_timeout: float = DEFAULT_REQUEST_TIMEOUT,
    retries: int = DEFAULT_RETRIES,
) -> spotipy.Spotify:
    """Get a Spotify client with the given scope.

    Args:
        scope (str): The OAuth scope to request. Defaults to
            "playlist-read-private".
        requests_timeout (float): Seconds to wait for a response before timing
            out. Defaults to 30.
        retries (int): Number of times to retry transient failures. Defaults to
            3.

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
        ),
        requests_session=_build_session(retries),
        requests_timeout=requests_timeout,
    )
    return sp
