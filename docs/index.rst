Spotify Playlists Extractor Documentation
==========================================

Welcome to the Spotify Playlists Extractor documentation! This tool automatically extracts and backs up all metadata from your Spotify playlists using the Spotify Web API.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api_reference
   examples
   troubleshooting

.. toctree::
   :maxdepth: 2
   :caption: API Documentation:

   modules

Overview
--------

The Spotify Playlists Extractor is a Python tool designed to:
   * Extract complete metadata from your Spotify playlists
   * Generate both full and cleaned JSON output files
   * Handle Spotify OAuth2 authentication automatically
   * Run periodically on backend servers for automated backups
   * Provide a simple command-line interface

Key Features
------------

* **Complete Metadata Extraction**: Pulls all available metadata for playlists, tracks, artists, and albums
* **Dual Output Format**: Generates both comprehensive and simplified JSON files
* **OAuth2 Authentication**: Handles Spotify authentication flow automatically
* **Configurable Limits**: Control the number of playlists to extract
* **Server-Friendly**: Designed for automated execution
* **Clean Architecture**: Well-structured, documented, and tested code

Quick Start
-----------

1. Install the package and dependencies:

   .. code-block:: bash

      uv venv
      source .venv/bin/activate
      uv sync

2. Set up your Spotify API credentials in a ``.env`` file
3. Run the extractor:

   .. code-block:: bash

      spotify-playlists-extractor -o ./output

For detailed installation and usage instructions, see the :doc:`installation` and :doc:`usage` sections.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
