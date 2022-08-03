#! python 3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments

import zipfile, os

os.chdir('C:\\delicious')

def backupToZip(folder):
    # Backup entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) #make sure folder is absolute path
    print('We got here')

    #Figure out the filename for this code based on files that exist (if 1 exists 2, etc)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1


    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s.....' % (foldername))
        #add current folder to zip file
        backupZip.write(foldername)
        #add all the files in this folder to ZIP file
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')



backupToZip("C:\\delicious\\date Change Test")
