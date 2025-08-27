Troubleshooting
===============

Installation Issues
-------------------

**uv not found**
   Install uv: ``curl -LsSf https://astral.sh/uv/install.sh | sh``

**Python version error**
   Ensure Python 3.10+: ``python --version``

**Permission denied**
   Check directory permissions or use different output directory

Authentication Issues
---------------------

**Invalid client credentials**
   * Verify ``.env`` file has correct Spotify app credentials
   * Check Spotify Developer Dashboard settings
   * Ensure no extra spaces in ``.env`` file

**Redirect URI mismatch**
   * Verify redirect URI in ``.env`` matches Spotify app settings
   * Must be exactly: ``https://127.0.0.1:8888/callback``

**Token expired**
   Delete cache and re-authenticate:

   .. code-block:: bash

      rm -rf ~/.cache/spotify-playlists-extractor/

Runtime Issues
--------------

**Network errors**
   * Check internet connection
   * Ensure access to ``api.spotify.com`` and ``accounts.spotify.com``

**Rate limiting**
   * Wait a few minutes and retry
   * Use smaller ``--limit`` value
   * Run during off-peak hours

**Empty output files**
   * Verify you have playlists in Spotify
   * Check if playlists are private
   * Increase ``--limit`` value

**JSON parsing errors**
   * Delete corrupted files and re-run
   * Check available disk space

Getting Help
------------

When reporting issues, include:
   * Error message
   * Python version (``python --version``)
   * Operating system
   * Command used

Never share your actual Spotify credentials when reporting issues.
