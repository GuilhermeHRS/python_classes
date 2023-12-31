# install and import the requests lib
import requests
import datetime
import os
from dotenv import load_dotenv
import tkinter as tk

load_dotenv()
API_KEY = os.getenv("API_KEY")

# there are a lot of ways to make your own api call in OpenWeather website 
city_name = "Caraguatatuba"
country_code = "BR"
api_call = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}"

# calling the api call
request = requests.get(api_call)
# showing the json pckge
dic_request = request.json()
# print(dic_request)

# getting datas in dic_request (this is a dictionary)
timestamp_day = dic_request['dt']
timestamp_sunrise = dic_request['sys']['sunrise']
timestamp_sunset = dic_request['sys']['sunset']

# formatting datas with datetime lib
dt_timestamp_day = datetime.datetime.fromtimestamp(timestamp_day)
dt_sunrise = datetime.datetime.fromtimestamp(timestamp_sunrise)
dt_sunset = datetime.datetime.fromtimestamp(timestamp_sunset)
format = "%H:%M:%S"
format_day = '%d/%m/%Y %H:%M:%S'

dt_timestamp_day = dt_timestamp_day.strftime(format_day)
sunriseTime = dt_sunrise.strftime(format)
sunsetTime = dt_sunset.strftime(format)
description = dic_request['weather'][0]['description']
weather = round(dic_request['main']['temp'] - 273)

# print(f"Day: {dt_timestamp_day}\nSunrise time: {sunriseTime}\nSunset time: {sunsetTime}\nTemperature in Celsius: {weather}°")

window = tk.Tk()
window.title("Weather Forecast")

width = 400
height = 200
window.geometry(f"{width}x{height}")

label_dt = tk.Label(window, text= f"Now: {dt_timestamp_day}")
label_dt.pack(pady=15)

label_sun = tk.Label(window, text=f"Sunrise: {sunriseTime} - Sunset: {sunsetTime}")
label_sun.pack(pady=2)

label_weather = tk.Label(window, text=f"Today it's {weather}° Celsius in {city_name}")
label_weather.pack(pady=1)

btn = tk.Button(window, text="Close", pady=3, width= 10, command=window.quit)
btn.pack()

window.mainloop(0)

