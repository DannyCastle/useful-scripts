#! python3
# tableMaker.py - Get's a list of lists with strings and puts em
# in a table that fits them.

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in tableData:
        colWidths[tableData.index(i)] = len(max(i, key=len))
    print(colWidths)
    maxWidth = max(colWidths)
    print('The max width is: ' + str(maxWidth))
    print('Table Data'.center((maxWidth + 1) * (len(tableData)), '-'))
    """count = 0
    for i in tableData[0]:
        print(str(i).rjust(maxWidth),end='')
        print(str(tableData[1][tableData[0].index(i)]).rjust(maxWidth),end='')
        print(str(tableData[2][tableData[0].index(i)]).rjust(maxWidth))


    for i in range(len(tableData)):
        print(str("""
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(maxWidth + 1), end='')
        print()








tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['Samsung', 'Nokia', 'LG', 'Motorola']]

printTable(tableData)
"""test = ['sdfsdfdfdf', 'asd']
long = len(max(test))
print(long)"""
