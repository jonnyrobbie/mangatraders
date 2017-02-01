#!/usr/bin/python
import sys, os, shutil
import urllib.request
from pyquery import PyQuery as pq
import zipfile

chapterLink = sys.argv[1]
responseCode = 0
pages = 0
nonemptyDir = False

while responseCode != 404:
    try:
        print("Downloading webpage", end=".....", flush=True)
        pageRequest = urllib.request.Request(chapterLink)
        pageRequest.add_header('User-agent', 'Wget1.18')
        pageResponse = urllib.request.urlopen(pageRequest)
        print(str(pageResponse.getcode()) + " OK")
        pages = pages + 1
        responseCode = pageResponse.getcode()
    except urllib.error.HTTPError:
        print("ERROR")
        responseCode = 404
    pageParse = pq(pageResponse.read().decode("utf-8"))
    if pages == 1:
        seriesName = pageParse(".IndexName").attr("value")
        curChapter = pageParse(".CurChapter").html()
        if seriesName is None or curChapter is None:
            responseCode = 404
            print("Invalid page!")
            break
        dirName = "/tmp/" + seriesName + "-" + curChapter.zfill(4)
        if not os.path.exists(dirName):
            os.mkdir(dirName)
        print("Series name: " + seriesName)
        print("Current chapter: " + curChapter)
        print("Directory name: " + dirName)
        print("==============================")
    if curChapter != pageParse(".CurChapter").html():
        print("Reached the end of the chapter.")
        break
    imgSrc = pageParse(".image-container .CurImage").attr("src")
    curPage = pageParse(".CurPage").html()
    nextPage = pageParse(".image-container a").attr("href")
    try:
        print("Image src: " + imgSrc)
        print("Downloading image " + str(curPage).zfill(3), end="...", flush=True)
        imageRequest = urllib.request.Request(imgSrc)
        imageRequest.add_header('User-agent', 'Wget1.18')
        imageResponse = urllib.request.urlopen(imageRequest)
        print(str(imageResponse.getcode()) + " OK")
        print("Saving image", end="............", flush=True)
        with open(dirName + "/" + str(curChapter).zfill(4) + "-" + str(curPage).zfill(3) + "." + imgSrc[-3:], "wb") as f:
            f.write(imageResponse.read())
            f.close()
        print("Done")
        nonemptyDir = True
    except:
        print("ERROR")
        print("Failed to fetch the image")
        print(sys.exc_info())
        break
    chapterLink = "http://mangatraders.biz" + nextPage
if nonemptyDir == True:
    try:
        print("Compressing", end=".............", flush=True)
        def zipdir(path, ziph):
            for root, dirs, files in os.walk(path):
                for file in files:
                    ziph.write(os.path.join(root, file), file)
        zf = zipfile.ZipFile(dirName + ".zip", "w", zipfile.ZIP_DEFLATED)
        zipdir(dirName + "/", zf)
        zf.close()
        print("Done")
    except:
        print("Compression error")
else:
    print("Failed to fetch any manga pages")
if dirName is not None:
    print("Removing tempdir", end="........", flush=True)
    shutil.rmtree(dirName)
    print("Done")

