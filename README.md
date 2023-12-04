This is EvenBetterHelp, a straightforward but simple calendar based journaling website. The site itself is based in Python, and the instructions for setting up, running, and accessing the site are found below.
- The site has been built and tested using Python 3.12.0. We recommend setting up a virtual environment using Python's included `venv` module, but this is not strictly necessary if you are just wanted to view the site.
- The provided `requirements.txt` holds all the needed modules for launching the site. Install these with `python3.12 -m pip install -requirements.txt`.
- In the same directory as the main `wsgi.py` file, execute `flask run` (optionally with `--debug` for debugging information).
- The site is should now be viewable on [http://localhost:5000](http://localhost:5000).