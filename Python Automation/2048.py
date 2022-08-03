#! python3
# 2048.py - Plays the 2048 game automatically

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
#Go to webpage
browser.get('http://2048game.com')
time.sleep(2)

#Press the buttons until end
htmlElem = browser.find_element_by_tag_name('html')

gameOver = ''
#loop the button
while gameOver == '':
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    try:
        gameOver = browser.find_element_by_class_name('game-message')
        gameOver = gameOver.text
        
    except:
        print('Exception occured')
        
    

print('You did it. Out of the loop now.')
