#! python3
# comicChecker.py  - Check comic websites and tells you if new comics are there

import time, datetime, bs4, os, sys, requests, threading, shelve
os.chdir('C:\\users\\daniel.castillo\\desktop\\python learning\\comic checking')

shelfFile = shelve.open('currentComicVersion')
#print(shelfFile['xkcd'])

def whichComic():
    print('Which comic do you want to check? Input 99 for All')
    print('1-XKCD, 2-LunarBaboon, 3-Savage Chickens')
    print('4-Extra Ordinary, 5-Wonderella, 6-Moonbeard, 7-HappleTea')
    choices = [1,2,3,4,5,6,7,99]
    if len(sys.argv) > 1:
        try:
            choice = int(sys.argv[2])
        except:
            print('Invalid argument.')
            choice = 0
    else:
        choice = 0
    while choice not in choices:
        print('Choose a number between 1 and 7.')
        try:
            choice = int(input())
        except:
            continue

    if choice == 99:
        checkAll()
    else:
        checkComic(choice)

def checkAll():
    checkComicThreads = []
    for i in range(1, 8):
        checkComicThread = threading.Thread(target=checkComic, args=[i])
        checkComicThreads.append(checkComicThread)
        checkComicThread.start()

    for thread in checkComicThreads:
        thread.join()

    print('All comics checked.')

    

def checkComic(choice):
    if choice == 1:
        comicName = 'xkcd'
        res = requests.get('https://xkcd.com')
        imgHtml = '#comic img'
        imgPrefix = 'https:'
    if choice == 2:
        comicName = 'Lunar Baboon'
        res = requests.get('http://www.lunarbaboon.com')
        imgHtml = '.journal-entry-text img'
        imgPrefix = '' #fucking stuck here weird as fuck image hosting
    if choice == 3:
        comicName = 'Savage Chickens'
        res = requests.get('https://www.savagechickens.com')
        imgHtml = '.copy-pad img'
        imgPrefix = ''
    if choice == 4:
        comicName = 'Extra Ordinary'
        res = requests.get('https://www.exocomics.com')
        imgHtml = '.comic img'
        imgPrefix = ''
    if choice == 5:
        comicName = 'Wonderella'
        res = requests.get('http://nonadventures.com')
        imgHtml = '#comic img'
        imgPrefix = ''
    if choice == 6:
        comicName = 'Moonbeard'
        res = requests.get('https://moonbeard.com')
        imgHtml = '#comic img'
        imgPrefix = ''
    if choice == 7:
        comicName = 'Happle Tea'
        res = requests.get('http://www.happletea.com')
        imgHtml = '#comic img'
        imgPrefix = ''
        
    print('Checking %s comics....' % (comicName))
    
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    comicElem = soup.select(imgHtml)
    shelfFile.setdefault(comicName, [])
    #shelfFile[comicName] = []
    if comicElem == []:
        print('Could not find comic image')
        return
    comicSource = comicElem[0].get('src')
    if comicSource == shelfFile[comicName]:
        currentTime = datetime.datetime.now()
        humanTime = currentTime.strftime('%B %d %I:%M %p')
        print('There has not been a new %s  as of ' % (comicName) + humanTime)
    else:
        try:
            comicUrl = imgPrefix + comicSource
            print('Downloading new comic...')
            res = requests.get(comicUrl)
            res.raise_for_status()
            os.makedirs(comicName, exist_ok=True)
            imageFile = open(os.path.join(comicName, os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
            shelfFile[comicName] = comicSource
            #print(comicElem[0].get('src'))
        except requests.exceptions.MissingSchema as err:
            #skip comic
            print('Missing Schema. Whatever that is. Skipping comic...')
            #print(err)
    return
            

whichComic()
shelfFile.close()
print('Done.')
