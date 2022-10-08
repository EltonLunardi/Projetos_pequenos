import requests
from pprint import pprint

API_Key = ''

city = input('Insira a cidade: ')
base_url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_Key+'&q='+city
weather_data = requests.get(base_url).json()

pprint(weather_data)