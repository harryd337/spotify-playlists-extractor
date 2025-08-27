Usage Guide
===========

Basic Usage
-----------

.. code-block:: bash

   spotify-playlists-extractor -o <output_directory> [-l <limit>]

**Options:**
   * ``-o, --output-dir``: Directory to save files (required)
   * ``-l, --limit``: Number of playlists to extract (default: 50)

Examples
--------

.. code-block:: bash

   # Extract all playlists
   spotify-playlists-extractor -o ./backup

   # Extract only 5 playlists
   spotify-playlists-extractor -o ./output -l 5

Authentication
--------------

On first run, the tool will open your browser to authenticate with Spotify. Grant permissions and you're set - the token is cached for future use.

Output Files
------------

The tool creates two files:
   * ``full_playlists.json`` - Complete Spotify API data
   * ``clean_playlists.json`` - Simplified format with just names, artists, albums

Automation
----------

For automated backups, add to crontab:

.. code-block:: bash

   # Daily backup at 2 AM
   0 2 * * * cd /path/to/project && source .venv/bin/activate && spotify-playlists-extractor -o /path/to/backup
