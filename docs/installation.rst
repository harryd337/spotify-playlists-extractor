Installation Guide
==================

Prerequisites
-------------

* Python 3.10+
* `uv package manager <https://github.com/astral-sh/uv>`_
* Spotify Developer Account

Quick Setup
-----------

.. code-block:: bash

   # Clone and setup
   git clone <repository-url>
   cd spotify-playlists-extractor

   # Create environment
   uv venv
   source .venv/bin/activate  # Linux/macOS
   # .venv\Scripts\activate   # Windows

   # Install dependencies
   uv sync

Spotify API Setup
-----------------

1. **Create Spotify App**:
      Go to `Spotify Developer Dashboard <https://developer.spotify.com/dashboard>`_, create an app, and set redirect URI to ``https://127.0.0.1:8888/callback``

2. **Configure Environment**:
   .. code-block:: bash

      cp .env.example .env
      # Edit .env with your Client ID and Client Secret

Verification
------------

.. code-block:: bash

   spotify-playlists-extractor --help

That's it! See :doc:`usage` for how to run the tool.
