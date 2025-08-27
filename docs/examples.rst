Examples
========

Basic Usage
-----------

.. code-block:: bash

   # Extract all playlists
   spotify-playlists-extractor -o ./backup

   # Extract first 10 playlists
   spotify-playlists-extractor -o ./output -l 10

   # Extract to specific directory
   spotify-playlists-extractor -o /home/user/spotify-backup

Automation Scripts
------------------

Daily Backup Script
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   #!/bin/bash
   # daily-backup.sh

   cd /path/to/spotify-playlists-extractor
   source .venv/bin/activate
   spotify-playlists-extractor -o "/backup/$(date +%Y-%m-%d)"

Cron Job
~~~~~~~~

.. code-block:: bash

   # Add to crontab (crontab -e)
   0 2 * * * /path/to/daily-backup.sh 2>&1 | logger -t spotify-backup

Data Processing
---------------

Analyze Playlists
~~~~~~~~~~~~~~~~~

.. code-block:: python

   import json
   from collections import Counter

   # Load clean playlist data
   with open('clean_playlists.json') as f:
       data = json.load(f)

   # Count artists
   artists = []
   for playlist in data['playlists']:
       for song in playlist['songs']:
           artists.extend(song['artists'])

   # Top 10 artists
   top_artists = Counter(artists).most_common(10)
   for artist, count in top_artists:
       print(f"{artist}: {count} songs")

Convert to CSV
~~~~~~~~~~~~~~

.. code-block:: python

   import json
   import csv

   with open('clean_playlists.json') as f:
       data = json.load(f)

   with open('playlists.csv', 'w', newline='') as f:
       writer = csv.writer(f)
       writer.writerow(['playlist', 'song', 'artists', 'album'])

       for playlist in data['playlists']:
           for song in playlist['songs']:
               writer.writerow([
                   playlist['name'],
                   song['name'],
                   '; '.join(song['artists']),
                   song['album']
               ])
