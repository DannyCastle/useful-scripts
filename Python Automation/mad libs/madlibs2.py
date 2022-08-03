#$ python3
# madlibs2.py - Will ask user to replace ADJECTIVE NOUN and VERBs.

import os, re



os.chdir("C:\\Users\\daniel.castillo\\Desktop\\Python Learning\\mad libs")

#Copied from stack overflow

#Open the file and save it to text variable
print('Where is the madlib file located? Please give absolute path (no quotes): ')
filePath = str(input())
file = open(filePath)
text = file.read()
file.close()

#regex for finding all ADJ NOUN and VERB. A group for each.

regex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)')

# for every match in the text (which each match will have two strings, one being '')
for i in regex.findall(text):
    #for every individual word in the matches
    for j in i:
        #as long as the word isn't empty
        if j != '':
            #This is saying, for every word, find the word (match every time)
            reg = re.compile(r'{}'.format(j))
            #Find the replacement for the word we're matching
            inp_text = input('Enter the substitute for %s: ' %j)
            #Sub in the replacement
            text = reg.sub(inp_text, text, 1)

print(text)

file = open('madlibs_ans.txt', 'w')
file.write(text)
file.close()
