#! python3
# stopwatch.py - Keep tracks of laps using enter key

import time

print('Press ENTER to begin. Press ENTER again to "click" the stopwatch.')
print('Press Ctrl-C to quit.')
input()  #Here's where ENTER is pressed
startTime = time.time()
print('Started.')
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lastTime = time.time() #reset last lap time
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
except KeyboardInterrupt:
    #Handle the Ctrl-C exception to keep its error message from displaying
    print('\nDone.')

    
