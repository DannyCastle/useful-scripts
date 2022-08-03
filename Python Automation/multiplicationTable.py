#! python3
# multiplactionTable.py - Takes an integer and creates a multiplication table

import os, openpyxl, sys
from openpyxl.utils import get_column_letter as N2L
from openpyxl.styles import Font

os.chdir('C:\\users\\daniel.castillo\\desktop\\python learning')

while len(sys.argv) > 2:
    print('Too many arguments. Just one argument (an integer) please.')

if len(sys.argv) == 1:
    print('Max multiplication value: ')
    try:
        mult = int(input())
    except:
        print('Idiot. Enter one number: ')
        mult = int(input())
else:
    mult = int(sys.argv[1])

wb = openpyxl.Workbook()
sheet = wb.active
boldFont = Font(bold=True)


for i in range(2, mult+2):
    col_cell = sheet['A'+str(i)]
    col_cell.value = i - 1
    col_cell.font = boldFont
    row_cell = sheet[N2L(i)+ '1']
    row_cell.value = i - 1
    row_cell.font = boldFont
    #sheet[N2L(i)+str(i)].value = 'test value'

for col in range(2, mult+2):
    for row in range(2, mult+2):
        sheet[N2L(col)+str(row)].value = (col - 1) * (row - 1)
        



wb.save('Multiplication table x%s.xlsx' % (mult))
