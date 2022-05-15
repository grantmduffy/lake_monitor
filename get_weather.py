import requests

with open('api_key.txt', 'r') as f:
    api_key = f.read()
lat, lon = 48.134143, -122.3029389
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

r = requests.get(url)
print(r)


