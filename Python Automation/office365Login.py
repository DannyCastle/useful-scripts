#! python3
# office365Login.py - Takes 2 arguements, and signs into Office 365

import sys, time
from selenium import webdriver


if len(sys.argv) != 3:
    print('What\'s your O365 email?')
    email = str(input())
    print('Ok, now what is your password?')
    passwd = str(input())
    print('Ok, logging you in now....')
    
else:
    email = sys.argv[1]
    passwd = sys.argv[2]
    

#email = sys.argv[1]
#passwd = sys.argv[2]
# Open selenium Firefox to that login.microsoftonline.com
browser = webdriver.Firefox()
browser.get('https://login.microsoftonline.com')


# Fill in the details of the login
emailElem = browser.find_element_by_id('i0116')
emailElem.send_keys(email)
nextButton = browser.find_element_by_id('idSIButton9')
nextButton.click()
time.sleep(2)
passwdElem = browser.find_element_by_id('i0118')
passwdElem.send_keys(passwd)
passwdElem.submit()
time.sleep(2)
noButton = browser.find_element_by_id('idBtn_Back')
noButton.click()

