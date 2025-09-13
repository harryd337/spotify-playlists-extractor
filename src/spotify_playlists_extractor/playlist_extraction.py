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
    playlists_items = []
    offset = 0
    batch_size = 50  # Hardcoded Spotify API limit per request (set by Spotify)
    remaining_limit = limit
    current_user_playlists = None
    while remaining_limit > 0:
        current_batch_size = min(batch_size, remaining_limit)
        current_user_playlists_batch = sp.current_user_playlists(
            limit=current_batch_size, offset=offset
        )
        if current_user_playlists is None:
            current_user_playlists = current_user_playlists_batch.copy()
            current_user_playlists.pop("items", None)
            current_user_playlists.pop("href", None)
            current_user_playlists.pop("next", None)
            current_user_playlists.pop("previous", None)
            current_user_playlists.pop("offset", None)
        for _, current_user_playlist in enumerate(
            current_user_playlists_batch["items"]
        ):
            playlist_spotify_id = current_user_playlist["id"]
            playlist_spotify_uri = f"spotify:playlist:{playlist_spotify_id}"
            playlist = sp.playlist(playlist_spotify_uri, additional_types=["track"])
            playlists_items.append(playlist)
        remaining_limit -= current_batch_size
        offset += batch_size
        if len(current_user_playlists_batch["items"]) < current_batch_size:
            break
    playlists = (
        current_user_playlists.copy() if current_user_playlists is not None else {}
    )
    playlists["items"] = playlists_items
    playlists["limit"] = limit
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
