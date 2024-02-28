import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
  print('\n*** Get Current Weather Conditions ***\n')

  city = input('\nPLease enter a city name:\n')

  request_url = 'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

  #print(request_url)

  weather_data= requests.get(request_url).json()
  #pprint(weather_data)

  print(f'\nCurrent weather for {weather_data["name"]}')
  print(f'\nThe temp is {weather_data["main"]["temp"]}')
  print(f'\nFeels like {weather_data["main"]["feels_lik"]} and {weather_data["weather"][0]["description"]}.')

if __name__ == "__main__":
  get_current_weather()
