#$ python3
# Multiclipboard - Will store multiple copies to paste
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - loads keyword to clipboard.
#           py.exe mcb.pyw list - loads all keywords to clipboard.


import pyperclip, shelve, sys, os

os.chdir('C:\\Users\\daniel.castillo\\Desktop\\Python Learning\\mcb')

mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])






mcbShelf.close()


