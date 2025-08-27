"""This module contains the functions to clean the playlist metadata."""

import json
from pathlib import Path


def clean_playlist_metadata(playlists: dict) -> dict:
    """Clean the playlist metadata.

    Args:
        playlists (dict): A dictionary containing the full playlists data.

    Returns:
        dict: A dictionary containing the cleaned playlists data.
    """
    cleaned_playlists: dict = {"playlists": []}

    # Extract playlist items from the input structure
    if "items" in playlists:
        for playlist_item in playlists["items"]:
            cleaned_playlist = {
                "name": playlist_item.get("name", ""),
                "description": playlist_item.get("description", ""),
                "creator": playlist_item.get("owner", {}).get("display_name", ""),
                "songs": [],
            }

            # Extract songs from tracks
            if "tracks" in playlist_item and "items" in playlist_item["tracks"]:
                for track_item in playlist_item["tracks"]["items"]:
                    if track_item.get("track"):
                        track = track_item["track"]
                        song = {
                            "name": track.get("name", ""),
                            "artists": [],
                            "album": track.get("album", {}).get("name", ""),
                        }

                        # Get all artist names
                        if track.get("artists"):
                            song["artists"] = [
                                artist.get("name", "")
                                for artist in track["artists"]
                                if artist.get("name")
                            ]

                        cleaned_playlist["songs"].append(song)

            cleaned_playlists["playlists"].append(cleaned_playlist)

    return cleaned_playlists


def save_cleaned_playlists(cleaned_playlists: dict, output_dir: str):
    """Save the cleaned playlists data to a JSON file.

    Args:
        cleaned_playlists (dict): A dictionary containing the cleaned playlists data.
        output_dir (str): The directory path where the JSON file should be saved.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / "clean_playlists.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(cleaned_playlists, f, indent=4, ensure_ascii=False)
