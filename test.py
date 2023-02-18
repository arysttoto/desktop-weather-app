import requests
weather_token = '{{ encrypted }}'
code_to_condition = {
    'Clear': 'Clear \U00002600',
    'Clouds': 'Cloudy \U00002601',
    'Rain': 'Rainy \U00002614',
    'Drizzle': 'Rainy \U00002614',
    'Thunderstorm': 'Thunderstorm \U000026A1',
    'Snow': 'Snowy \U0001F32B',
    'Mist': 'Mist \U0001F32B'
}
def get_weather():
    city = input('city: ')
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric')
    data = r.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    condition = data['weather'][0]['main']
    condition = code_to_condition[condition]
    visibility = int(data['visibility'])/1000
    print(data)
get_weather()

