#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY format to
# European DD-MM-YYYY format

import shutil, os, re

os.chdir("C:\\delicious\\date Change Test")
#Create Regex to ID american file names
datePattern = re.compile(r'''^(.*?) #All text before the date
    ((0|1)?\d)-                     #one or two digit month
    ((0|1|2|3)?\d)-                 #one or two digits for the day
    ((19|20)\d\d)                   #four digit year
    (.*?)$                          #all text after the date
    ''', re.VERBOSE)


#Loop over files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    #Skip files without date
    if mo == None:
        continue

    #Get the different parts of the filename into variables
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming "%s" to "%s"....' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)  #We will uncomment after test


