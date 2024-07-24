import requests
from dotenv import load_dotenv
import os

# Loading ENV
load_dotenv()

# Constants
URI = "http://api.weatherapi.com/v1/current.json"
TOKEN = os.getenv('TOKEN')


def weather(city, lang='en'):
  """
  This function fetches weather information
  from the given city. Optional param is language.
  """
  
  # Configs
  params = {
    'key': TOKEN,
    'q': city,
    'lang': lang
  }

  # Network Request
  res = requests.get(URI, params)

  # Converting from json
  data = res.json()

  # If location not found handle  
  if 'error' in data:
    print("Location not found")
    return

  # Destructuring Useful Data
  forecast = {
    'temp_c': data['current']['temp_c'],
    'temp_f': data['current']['temp_f'],
    'condition': data['current']['condition']['text'],
    'state': data['location']['region']
  }
  
  print(forecast)

# help(weather)
  
user_location = input("Enter a location: ")
user_lang = input("Enter lang code (en=English): ")
weather(user_location, user_lang)