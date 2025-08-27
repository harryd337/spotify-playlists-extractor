"""Core module for spotify_playlists_extractor."""

import argparse

from .auth import get_spotify_client
from .playlist_extraction import extract_playlists, save_full_playlists
from .playlist_metadata_cleaning import clean_playlist_metadata, save_cleaned_playlists


def main():
    """Main function to run the app."""
    parser = argparse.ArgumentParser(
        description="This app uses the Spotify API to pull the user's playlists' \
metadata."
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        required=True,
        help="Directory where playlist metadata will be saved to",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        required=False,
        default=50,
        help="Number of playlists to extract",
    )
    args = parser.parse_args()
    sp = get_spotify_client()
    playlists = extract_playlists(sp, args.limit)
    save_full_playlists(playlists, args.output_dir)
    cleaned_playlists = clean_playlist_metadata(playlists)
    save_cleaned_playlists(cleaned_playlists, args.output_dir)
