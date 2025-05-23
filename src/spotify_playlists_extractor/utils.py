"""General Utility functions for spotify_playlists_extractor."""

import os
from pathlib import Path

import toml


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).resolve().parent.parent.parent


def get_package_root() -> Path:
    """Returns package root folder."""
    return Path(__file__).resolve().parent


def about() -> str:
    """Standard greeter function.

    Gives the documents something to cover regarding the project. The project
    information is extracted from pyproject.toml.

    Returns:
        Information about the project and key contacts.

    Example:
        >>> about()
        "Project Name: PROJECT_NAME
        Project Summary: PROJECT_SUMMARY
        Author Name: AUTHOR_NAME
        Author Contact: AUTHOR_CONTACT
    """
    parent_folder = Path(__file__).resolve().parent.parent.parent
    config_file = Path(parent_folder / "pyproject.toml")
    config = toml.load(config_file)
    return (
        f"Project Name: {config['tool']['poetry']['name']}\n"
        f"Project Description: {config['tool']['poetry']['description']}\n"
        f"Authors: {config['tool']['poetry']['authors']}\n"
    )


def create_folder(folder_path: str):
    """Create a folder if it does not exist."""
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except PermissionError as e:
            raise PermissionError(
                f"Permission Denied: Could not create folder '{folder_path}'. Make \
sure you have the required permissions."
            ) from e
