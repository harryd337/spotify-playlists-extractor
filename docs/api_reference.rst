API Reference
=============

This section provides documentation for the main modules and functions.

.. currentmodule:: spotify_playlists_extractor

Core Module
-----------

.. automodule:: spotify_playlists_extractor.core
   :members:
   :no-index:

Authentication Module
---------------------

.. automodule:: spotify_playlists_extractor.auth
   :members:
   :no-index:

Playlist Extraction Module
---------------------------

.. automodule:: spotify_playlists_extractor.playlist_extraction
   :members:
   :no-index:

Playlist Cleaning Module
-------------------------

.. automodule:: spotify_playlists_extractor.playlist_metadata_cleaning
   :members:
   :no-index:

Settings Module
---------------

.. automodule:: spotify_playlists_extractor.settings
   :members:
   :no-index:

Data Structures
---------------

Clean Playlist Format
~~~~~~~~~~~~~~~~~~~~~

The ``clean_playlists.json`` file follows this structure:

.. code-block:: python

   {
       "playlists": [
           {
               "name": "string",
               "description": "string",
               "creator": "string",
               "songs": [
                   {
                       "name": "string",
                       "artists": ["string", ...],
                       "album": "string"
                   }
               ]
           }
       ]
   }

Environment Variables
---------------------

Required environment variables in ``.env`` file:

* ``SPOTIFY_CLIENT_ID`` - Your Spotify app's Client ID
* ``SPOTIFY_CLIENT_SECRET`` - Your Spotify app's Client Secret
* ``SPOTIFY_REDIRECT_URI`` - OAuth redirect URI (default: ``https://127.0.0.1:8888/callback``)
