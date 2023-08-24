# install and import the requests lib
import requests
import datetime

# open the 'OpenWeather' website and generate your key
API_KEY = "1617be6066a665d681c8ec134b36c51f"

# there are a lot of ways to make your own api call in OpenWeather website 
city_name = "Caraguatatuba"
country_code = "BR"
api_call = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}"

request = requests.get(api_call)
dic_request = request.json()
# print(dic_request)

timestamp_day = dic_request['dt']
format_day = '%d/%m/%Y %H:%M:%S'
timestamp_sunrise = dic_request['sys']['sunrise']
timestamp_sunset = dic_request['sys']['sunset']

dt_timestamp_day = datetime.datetime.fromtimestamp(timestamp_day)
dt_sunrise = datetime.datetime.fromtimestamp(timestamp_sunrise)
dt_sunset = datetime.datetime.fromtimestamp(timestamp_sunset)
format = "%H:%M:%S"

dt_timestamp_day = dt_timestamp_day.strftime(format_day)
sunriseTime = dt_sunrise.strftime(format)
sunsetTime = dt_sunset.strftime(format)
description = dic_request['weather'][0]['description']
weather = round(dic_request['main']['temp'] - 273)


print(f"Day: {dt_timestamp_day}\nSunrise time: {sunriseTime}\nSunset time: {sunsetTime}\nTemperature in Celsius: {weather}°")