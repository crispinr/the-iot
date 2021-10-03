#micropython program to display the weather report of a particular location using oled and weather api

import ssd1306
import ujson as json
import urequests as requests
from machine import Pin, I2C

i2c = I2C(sda=Pin(16), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

#user data input
country_code = input("Enter the country code: ")
city = input("Enter the city name: ")

#openweather api call
weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_code + "&APPID=b190a0605344cc4f3af08d0dd473dd25"
weather_data = requests.get(weather_url)

#location of the weather report
location = weather_data.json().get("name") + " - " + weather_data.json().get("sys").get("country")

#description of the weather
description = "Desp: " + weather_data.json().get("weather")[0].get("main")

#temperature info
raw_temperature = weather_data.json().get("main").get("temp")-273.15
temperature = "Temp: " + str(raw_temperature) + "*C"

#humidity info
humidity = "Humid: " + str(weather_data.json().get("main").get("humidity")) + "%"

#wind info
wind = "Wind: " + str(weather_data.json().get("wind").get("speed")) + "mps"

#oled commands
display.text(location, 17, 0, 1)
display.text(description, 0, 20, 1)
display.text(humidity, 0, 30, 1)
display.text(wind, 0, 40, 1)
display.text(temperature, 0, 50, 1)
display.show()

#kindly check the output image in the root directory!
