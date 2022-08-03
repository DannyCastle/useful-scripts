#! python3
# quickWeather.py - Printer weather forcast for command line location

import json, requests, sys, re, pprint

if len(sys.argv) < 2:
    print('What is your city name or zip code? ')
    userInput = input()
    location = re.sub("\s", ',', userInput.strip())
else:
    location = ','.join(sys.argv[1:])

print(location)

#DOWNLOAD JSON FROM OPENWEATHER
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=580c718c1dc6d5a74351331659ec3d7e' % (location)
response = requests.get(url)
response.raise_for_status()

#Load JSON into Python
weatherData = json.loads(response.text)
#Print weather data
w = weatherData['weather']
print('Current weather in %s:' % (location))
print(w[0]['main'] + ' - ' + w[0]['description'])
print()
pprint.pprint(weatherData)
