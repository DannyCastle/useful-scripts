#! python3
# readCensusExcel.py - Gets population from each county

import openpyxl, pprint, os
os.chdir('C:\\users\\daniel.castillo\\desktop\\Py learning')
print('Opening workbook.....')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

#Fill in countyData with each county's pop
print('Reading rows....')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C'+ str(row)].value
    pop = sheet['D' + str(row)].value

    #this makes sure that the key for this state exists
    countyData.setdefault(state, {})
    # This makes sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    #Each row is one census tract, so increment by one.
    countyData[state][county]['tracts'] += 1
    #Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)
    

# Open new text file and write countyData to it
print('Writing results....')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')
