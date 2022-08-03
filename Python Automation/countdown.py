#! python3
# countdown.py - Countdown program that plays a sound

import time, subprocess, os
os.chdir('C:\\users\\daniel.castillo\\desktop\\python learning')


timeLeft = 10
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

#play sound file
subprocess.Popen(['start', 'alarm.wav'], shell=True)
