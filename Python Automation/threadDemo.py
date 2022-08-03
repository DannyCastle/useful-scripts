#! python3
# threadDemo.py - Demo multithreading

import threading, time
print('Start of program.')


def takeANap():
    time.sleep(5)
    print('Wake Up! Grab a brush and put a little  makeup!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')
