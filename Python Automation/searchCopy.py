#! python3
# search and copy - find .pdf and .jpg and move em
# searchCopy.py


import shutil, os
os.chdir("C:\\delicious")

def movePDFandPNG(folder, destination): #folder and destination are path strings
    folder = os.path.abspath(folder)
    os.chdir(folder)
    #print('we got here')
    #print(folder)


    for foldername, subfolders, filenames in os.walk(folder):
        for file in filenames:
            #newBase = os.path.basename(folder)
            #print(newBase)
            #print(os.path.abspath(filename))
            #ext = str(filename.endswith)
            #print(ext)
            if file.endswith('.pdf') or file.endswith('.PDF'):
                print('moving PDF: %s' % (file))
                shutil.copy(os.path.abspath(file), destination)
                
            elif file.endswith('.PNG') or file.endswith('.png'):
                print('moving PNG: %s' % (file))
                shutil.copy(os.path.abspath(file), destination)
                
            else:
                print('Not a PNG or PDF')

                

movePDFandPNG('C:\\delicious\\copyFrom', 'C:\\delicious\\copyTo')
