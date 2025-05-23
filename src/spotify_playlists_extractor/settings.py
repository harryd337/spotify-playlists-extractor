"""Settings for the spotify_playlists_extractor package."""

from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the spotify_playlists_extractor package."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra fields that are not defined in the model
    )

    # Spotify API credentials
    SPOTIFY_CLIENT_ID: str
    SPOTIFY_CLIENT_SECRET: str


@cache
def get_settings():
    """Get the settings for the spotify_playlists_extractor package."""
    return Settings()
