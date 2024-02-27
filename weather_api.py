import json
from model import Weather, dt
from dotenv import load_dotenv
from typing import Final
import requests
import os

load_dotenv()

API_KEY: Final[str] = os.getenv("API_KEY")
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather(city_name: str, mock: bool = True, ) -> dict:
    if mock:
        with open('data.json') as file:
            return json.load(file)

    # Request live data
    payload: dict = {'q': city_name, 'appid': API_KEY, 'units': 'imperial'}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    # Put mock data in file automatically

    # with open('data.json', 'w') as file:
    #     json.dump(data, file)

    return data


def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get('list')

    if not days:
        raise Exception(f'Problem with json: {weather}')

    weather_list: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description'))
        weather_list.append(w)

    return weather_list

# Check

# if __name__ == '__main__':
#     current_weather: dict = get_weather('tokyo', mock=True)
#     weather: list[Weather] = get_weather_details(current_weather)
#
#     for w in weather:
#         print(w)
    # Mock data
    # print(get_weather('', mock=True))
    # Real data
    # print(get_weather('thailand', mock=False))


