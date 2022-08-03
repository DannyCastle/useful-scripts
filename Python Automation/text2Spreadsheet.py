#! python3
# text2Spreadsheet.py - reads lines from text files and pastes to spreadsheet

import sys, openpyxl, os
from openpyxl.utils import get_column_letter as N2L

os.chdir('C:\\users\\daniel.castillo\\desktop\\python learning')
fileList = []
while True:
    if len(sys.argv) == 3:
        fileList.appen(sys.argv[2])
        fileList.append(sys.argv[3])
        break
    else:
        print('What is the path of the first file?')
        fileList.append(input())
        print('What is the path of the second file?')
        fileList.append(input())
        print('What is the path of the third file? If no more, input nothing.')
        userInput = input()
        while userInput != '':            
            fileList.append(userInput)
            print('Type path of next file (if no more, input nothing):')
            userInput = input()
        break

    
wb = openpyxl.Workbook()
sheet = wb.active
fileCounter = 1
for filename in fileList:
    file = open(filename)
    i = 1
    for line in file.readlines():
        sheet[N2L(fileCounter) + str(i)].value = line
        i += 1
    fileCounter += 1
    file.close()

print('Saving file in working directory....')
wb.save('line2Spreadsheet.xlsx')


