#! python3
# multidownloadXKCD.py - Download XKCD multithread

import requests, os, bs4, threading
os.chdir('C:\\users\\daniel.castillo\\desktop\\python learning')
os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic + 1):
        #download page
        print('Downloading page https://xkcd.com/%s....' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="html.parser")

        #Find the URL of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            try:
                comicUrl = 'http:' + comicElem[0].get('src')
                #download image
                print('Downloading image %s....' % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()
            except requests.exceptions.MissingSchema:
                #skip this comic
                print('Skipping comic....')
                continue


            #Save image to .\xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


# TODO: Create and start thread objects
downloadThreads = []
for i in range(1, 51, 10):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 9))
    downloadThreads.append(downloadThread)
    downloadThread.start()
    
#TODO: wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
