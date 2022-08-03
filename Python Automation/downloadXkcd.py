#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'
os.chdir('C:\\Users\\daniel.castillo\\desktop\\python learning')
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('2100/'):
    #Download the page
    print('Downloading page %s....' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    #Find the url of the comic img
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            #Download the image
            print('Downloading image %s....' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip this comic
            print('Skipping comic...')
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
            continue
        #Save image to .\xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #Get Prev button URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')


print('Done.')
