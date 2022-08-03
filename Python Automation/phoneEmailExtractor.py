#! python3
# phoneEmailExtractor.py - Just as the name says,
# but extracts from clipboard

import pyperclip
import pprint
import re

commaRegex = re.compile(r'''(
    



    )''', re.VERBOSE)



phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          # area code
    (\s|-|\.)?                  # separator
    (\d{3})                     # first 3 digits
    (\s|-|\.)?                  # separator
    (\d{4})                     # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?# possible extension
    )''', re.VERBOSE)


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username (whaat? % sign in an email?)
    @                   # @ symbol
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})    # dot-something
    )''', re.VERBOSE)


text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    if groups[1] == '':
        phoneNum = '-'.join([groups[3], groups[5]])
    else:
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
           phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')




