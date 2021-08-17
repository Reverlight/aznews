import requests

from credentials import OPEN_WEATHER_MAP_API_KEY


def api_request(url):
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        return r
    except requests.exceptions.HTTPError as err:
        print("Http Error:", err)
    except requests.exceptions.ConnectionError as err:
        print("Error Connecting:", err)
    except requests.exceptions.Timeout as err:
        print("Timeout Error:", err)
    except requests.exceptions.RequestException as err:
        print("Unknown error:", err)


def get_city_weather(city):
    url = f' https://api.openweathermap.org/data/2.5/weather' \
          f'?q={city}' \
          f'&appid={OPEN_WEATHER_MAP_API_KEY}' \
          f'&units=metric'

    r = api_request(url)
    if r:
        r_json = r.json()
        weather_description = r_json['weather'][0]['description'].capitalize()
        city_temp = round(r_json['main']['temp'])
        city_info = f'{city_temp}ºc. {weather_description}. {city}'
        return city_info
    return 'Error'
