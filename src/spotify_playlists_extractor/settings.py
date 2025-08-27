"""Settings for the spotify-playlists-extractor package."""

from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the spotify-playlists-extractor package."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra fields that are not defined in the model
    )
    SPOTIFY_CLIENT_ID: str
    SPOTIFY_CLIENT_SECRET: str
    SPOTIFY_REDIRECT_URI: str


@cache
def get_settings():
    """Get the settings for the spotify-playlists-extractor package."""
    return Settings()
