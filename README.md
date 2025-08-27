# Spotify Playlists Extractor

A Python tool that uses the Spotify Web API to automatically extract and backup all metadata from your Spotify playlists. This tool is designed to run periodically on a backend server to ensure your playlist data is safely backed up.

## Features

- **Complete Metadata Extraction**: Pulls all available metadata for your playlists including tracks, artists, albums, and playlist details
- **Dual Output Format**: Generates both full metadata JSON files and cleaned versions with essential information
- **Automatic Authentication**: Handles Spotify OAuth2 authentication flow
- **Configurable Limits**: Control how many playlists to extract per run
- **Server-Friendly**: Designed for automated execution on backend servers
- **Clean Data Structure**: Outputs well-structured JSON files for easy processing

## Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Spotify Developer Account and App credentials

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd spotify-playlists-extractor
```

### 2. Set Up Python Environment with uv

First, create a virtual environment:

```bash
uv venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```

### 3. Spotify API Setup

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app or use an existing one
3. Note down your `Client ID` and `Client Secret`
4. Add `https://127.0.0.1:8888/callback` to your app's Redirect URIs in the Spotify app settings

### 4. Environment Variables Configuration

Copy the example environment file:

```bash
cp .env.example .env
```

Edit the `.env` file with your Spotify app credentials:

```bash
SPOTIFY_CLIENT_ID="your_actual_client_id_here"
SPOTIFY_CLIENT_SECRET="your_actual_client_secret_here"
SPOTIFY_REDIRECT_URI="https://127.0.0.1:8888/callback"
```

**Important**:
- Replace the placeholder values with your actual Spotify app credentials
- The redirect URI should match exactly what you set in your Spotify app settings
- Keep the `.env` file secure and never commit it to version control

## Usage

### Command Line Interface

The tool provides a command-line interface with the following options:

```bash
spotify-playlists-extractor -o <output_directory> [-l <limit>]
```

**Required Arguments:**
- `-o, --output-dir`: Directory where playlist metadata will be saved

**Optional Arguments:**
- `-l, --limit`: Number of playlists to extract (default: 50)

### Examples

Extract all playlists (up to 50) and save to `./output` directory:
```bash
spotify-playlists-extractor -o ./output
```

Extract only the first 10 playlists:
```bash
spotify-playlists-extractor -o ./output -l 10
```

Extract playlists to a specific backup directory:
```bash
spotify-playlists-extractor -o /path/to/backup/spotify-playlists
```

### First Run Authentication

On your first run, the tool will:
1. Open your web browser to the Spotify authorization page
2. Ask you to log in and grant permissions
3. Redirect you to the callback URL
4. Cache the authentication token for future runs

## Output Files

The tool generates two JSON files in the specified output directory:

### 1. `full_playlists.json`
Contains complete metadata from the Spotify API, including:
- All playlist information (name, description, owner, followers, etc.)
- Complete track details (duration, popularity, preview URLs, etc.)
- Full artist information (genres, popularity, external URLs, etc.)
- Album metadata (release dates, images, track counts, etc.)
- Spotify URIs and IDs for all entities

### 2. `clean_playlists.json`
Contains a simplified, clean version with essential information:
- Playlist name, description, and creator
- Song names, artists, and albums
- Structured for easy reading and processing

Example structure:
```json
{
    "playlists": [
        {
            "name": "My Awesome Playlist",
            "description": "Great songs for coding",
            "creator": "username",
            "songs": [
                {
                    "name": "Song Title",
                    "artists": ["Artist 1", "Artist 2"],
                    "album": "Album Name"
                }
            ]
        }
    ]
}
```

## Automated Execution

For server deployment, you can set up automated execution using:

### Cron Job
Add to your crontab to run daily at 2 AM:
```bash
0 2 * * * cd /path/to/spotify-playlists-extractor && source .venv/bin/activate && spotify-playlists-extractor -o /path/to/backup/directory
```

### Systemd Timer
Create a systemd service and timer for more robust scheduling.

### Docker
The tool can be containerized for easier deployment and management.

## Development

### Development Dependencies

Install development dependencies:
```bash
uv sync --group dev
```

### Code Quality

The project uses several code quality tools configured via pre-commit hooks:
- **Ruff**: Linting and formatting
- **Mypy**: Type checking
- **Bandit**: Security linting
- **Pre-commit hooks**: Various code quality checks

Install pre-commit hooks:
```bash
pre-commit install
```

Run pre-commit on all files:
```bash
pre-commit run --all-files
```

### Documentation

Build documentation:
```bash
cd docs
make html
```

## Project Structure

```
spotify-playlists-extractor/
├── src/spotify_playlists_extractor/
│   ├── __init__.py
│   ├── auth.py              # Spotify authentication
│   ├── core.py              # Main application logic
│   ├── playlist_extraction.py    # Playlist data extraction
│   ├── playlist_metadata_cleaning.py  # Data cleaning functions
│   └── settings.py          # Configuration management
├── docs/                    # Sphinx documentation
├── example_output/          # Example output files
├── pyproject.toml          # Project configuration
├── .env.example            # Environment variables template
└── README.md               # This file
```

## API Rate Limits

The Spotify Web API has rate limits. The tool handles these automatically, but for large numbers of playlists, consider:
- Running during off-peak hours
- Implementing delays between requests if needed
- Monitoring API usage in your Spotify Developer Dashboard

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the test suite and code quality checks
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
