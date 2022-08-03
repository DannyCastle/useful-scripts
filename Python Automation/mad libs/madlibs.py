#$ python3
# madlibs.pyw - Will ask user to replace ADJECTIVE NOUN and VERBs.

import shelve, os, re



os.chdir("C:\\Users\\daniel.castillo\\Desktop\\Python Learning\\mad libs")

adjectiveRegex = re.compile('ADJECTIVE')
nounRegex = re.compile('NOUN')
verbRegex = re.compile('VERB')


#TODO: Ask user for the text file path



#TODO: Read text file
libsFile = open('test.txt', 'r')
libsString = str(libsFile.readlines())
print(libsString)

#TODO: Replace keywords, ask user for input
moA = adjectiveRegex.findall(libsString)
moV = verbRegex.findall(libsString)
moN = nounRegex.findall(libsString)

print(moA)

for adj in moA:
    print('Choose an adjective: ')
    moA[moA.index(adj)] = input()

print(moA)

    

#TODO: Export to new file
