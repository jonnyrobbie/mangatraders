# Mangatraders download script
Mangatraders has borked chapter download functionality. This script is for automated manga pages download and compression. It is simple, it tries to download all pages from a given chapter, and when it reaches a page that 404s, it compresses them all.

Usage:

    ./mangatraders.py Series-name chapter

This script is not robust at all, does not perform any input checking etc...! It may not work for you. Use at your own risk. Any pull requests are welcome.

Don't forget to `chmod +x`.
