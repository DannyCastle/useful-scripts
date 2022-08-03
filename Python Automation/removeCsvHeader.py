#! python3
# removeCsvHeader.py - Removes first row from all CSVs in folder

import csv, os

os.chdir('C:\\users\\daniel.castillo\\desktop\\python learning\csv learning')

os.makedirs('headerRemoved', exist_ok=True)

suffix = '.csv'
#Loop through all files in a folder
#Currently in csv learning folder
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '.....')
    #TODO: Read CSV file without first row
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    #TODO: Write out CSV file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
    
