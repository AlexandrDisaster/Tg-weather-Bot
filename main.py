from config import open_weather_token
from pprint import pprint
import requests
import datetime

def get_weather(city, token):
    try:
        r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={open_weather_token}")
        data = r.json()
        a = data[0]

        first_location = data[0]

        name = first_location['name']
        country = first_location['country']
        lat = first_location['lat']
        lon = first_location['lon']

        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={open_weather_token}&units=metric")
        data = r.json()

        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data['weather'][0]['description']
        wind = data["wind"]["speed"]

        print(f"""***Location: {name}, country: {country}, Coordinates: {lat}, {lon}***
        ***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*** \n Weather in {name}:\n Temperature: {cur_weather} ℃ \n Humidity: {humidity} % \n Weather: {weather} \n Wind: {wind} km/h""")


        return(f"""Location: {name}, \n country: {country}, \n Coordinates: {lat}, {lon} \n
        ***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*** \n Weather in {name}:\n Temperature: {cur_weather} ℃ \n Humidity: {humidity} % \n Weather: {weather} \n Wind: {wind} km/h""")
        
    except Exception as ex:
        print(ex)
        print("Check city name")

def main(city):
    return(get_weather(city, open_weather_token))

if  __name__ == '__main__':
    main()