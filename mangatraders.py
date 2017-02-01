#!/usr/bin/python
import sys, os, shutil
import urllib.request
import zipfile

server = "http://217.23.10.62/manga/"
series = sys.argv[1]
chapter = sys.argv[2]
dirname = "/tmp/" + series + "-" + chapter.zfill(4)
page = 0
responseCode = 0
def urlname():
    return server + series + "/" + chapter.zfill(4) + "-" + str(page).zfill(3) + ".png"
if not os.path.exists(dirname):
    os.mkdir(dirname)

while responseCode != 404:
    try:
        page = page + 1
        print("Retrieving " + urlname())
        response = urllib.request.urlopen(urlname())
        print("HTTP Response: " + str(response.getcode()))
        responseCode = response.getcode()
        with open(dirname + "/" + chapter.zfill(4) + "-" + str(page).zfill(3) + ".png", "wb") as f:
            f.write(response.read())
    except urllib.error.HTTPError:
        print("HTTP Error " + str(sys.exc_info))
        responseCode = 404
        page = page - 1
print("Successfully retrieved " + str(page) + " pages.")
if page > 0:
    try:
        print("Compressing")
        def zipdir(path, ziph):
            for root, dirs, files in os.walk(path):
                for file in files:
                    ziph.write(os.path.join(root, file))

        zf = zipfile.ZipFile(dirname + ".zip", "w", zipfile.ZIP_DEFLATED)
        zipdir(dirname + "/", zf)
        zf.close()
        print("Done")
    except:
        print("Error in compression")
else:
    print("Error, failed to download any pages!")
    print("The series/chapter is not on the download server.")
print("Removing temp directory")
shutil.rmtree(dirname)
