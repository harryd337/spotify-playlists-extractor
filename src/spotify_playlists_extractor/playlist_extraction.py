"""This module contains the functions to extract user playlists from the Spotify API."""

import json
from pathlib import Path

import spotipy


def extract_playlists(sp: spotipy.Spotify, limit: int = 50) -> dict:
    """Extract playlists from the Spotify API.

    Args:
        sp (spotipy.Spotify): A Spotify client.
        limit (int): The number of playlists to extract.

    Returns:
        dict: A dictionary containing the playlists.
    """
    current_user_playlists = sp.current_user_playlists(limit=limit)
    playlists_items = []
    for _, current_user_playlist in enumerate(current_user_playlists["items"]):
        playlist_spotify_id = current_user_playlist["id"]
        playlist_spotify_uri = f"spotify:playlist:{playlist_spotify_id}"
        playlist = sp.playlist(playlist_spotify_uri, additional_types=["track"])
        playlists_items.append(playlist)
    playlists = current_user_playlists.copy()
    playlists["items"] = playlists_items
    return playlists


def save_full_playlists(playlists: dict, output_dir: str):
    """Save the full playlists data to a JSON file.

    Args:
        playlists (dict): A dictionary containing the full playlists data.
        output_dir (str): The directory path where the JSON file should be saved.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / "full_playlists.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(playlists, f, indent=4, ensure_ascii=False)
