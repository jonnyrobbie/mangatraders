# Mangatraders download script
Mangatraders has borked chapter download functionality. This script is for automated manga pages download and compression. It is simple, it tries to download all pages from a given chapter, and when it reaches a page that 404s, it compresses them all.

Usage:

    mangatraders.py Series-name chapter

Example:

	mangatraders.py Kangoku-Gakuen 240

This script is not robust at all, does not perform any input checking etc...! It may not work for you. Use at your own risk. Any pull requests are welcome.

# Mangatraders download script v2
The first version downloads directly from one of their hosting servers. However some series are not uploaded there and thus the script may fail. this v2 scrapes the actual online reader page, so it should be more robust that way, but may be a bit slower. Though the disclaimers still apply. I suggest trying the v1 first and if it fails, try v2.

You may also be required to install pyquery module:

    pip pyquery

Usage:

    mt_scrape.py Online-reader-link

Example:

    mt_scrape.py http://mangatraders.biz/read-online/Akame-Ga-Kiru-chapter-73-page-1.html

* Both scripts' default tempdir is `/tmp/`. If you wish to have something else, you have to edit the scipt.
* Don't forget to `chmod +x`.
