#! python3
# lucky.py - Opens the first several top hits on Google for a search

import sys, webbrowser, requests, bs4

print('Googling...')# display text while downloading the Googs
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#Retrieve top search result
soup = bs4.BeautifulSoup(res.text)

#Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(3, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
