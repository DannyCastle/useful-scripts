#! python3
# musicLabeler.py - Change my music and add artist - My first program!!!

import re, os, mutagen, shutil
from mutagen.mp3 import EasyMP3 as MP3

#Group 1 = Title, 2 = space dash space, 3 = Artist, 4 = .mp3
mp3Regex = re.compile(r'([a-zA-Z0-9\s]+)(\s-\s{1})([a-zA-Z0-9\.\s]+)(\.mp3)')


os.chdir("C:\\Users\\daniel.castillo\\Desktop\\music")


def renameFiles(folder):
    for root, subfolders, files in os.walk(folder):
        for file in files:
            mo = mp3Regex.search(file)
            print('Renaming file: ' + file)
            newFilename = mo.group(1) + mo.group(4)
            shutil.move(os.path.join(root, file), 'C:\\Test\\%s' % (str(newFilename)))

def setArtist(folder):
    for root, subfolders, files in os.walk(folder):
        for file in files:
            print('Setting artist: ' + file)
            audio = MP3(file)
            mo = mp3Regex.search(file)
            audio['albumartist'] = mo.group(3)
            audio.save()


musicFolder = "C:\\Users\\daniel.castillo\\Desktop\\music"
setArtist(musicFolder)
renameFiles(musicFolder)
