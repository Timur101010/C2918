# print_user_agent.py
import requests

json = requests.get('http://httpbin.org/user-agent').json()
print(json['user-agent'])

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

# cli.py
import click

@click.command()
def main():
    print("I'm a beautiful CLI ✨")

if __name__ == "__main__":
    main()

var = {
    "base": "stations",
    "clouds": {
        "all": 90
    },
    "cod": 200,
    "coord": {
        "lat": 51.51,
        "lon": -0.13
    },
    "dt": 1485789600,
    "id": 2643743,
    "main": {
        "humidity": 81,
        "pressure": 1012,
        "temp": 280.32,
        "temp_max": 281.15,
        "temp_min": 279.15
    },
    "name": "London",
    "sys": {
        "country": "GB",
        "id": 5091,
        "message": 0.0103,
        "sunrise": 1485762037,
        "sunset": 1485794875,
        "type": 1
    },
    "visibility": 10000,
    "weather": [
        {
            "description": "light intensity drizzle",
            "icon": "09d",
            "id": 300,
            "main": "Drizzle"
        }
    ],
    "wind": {
        "deg": 80,
        "speed": 4.1
    }
}


import requests

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'http://samples.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    # дальше всё остаётся как было
    ...

@click.command()
@click.argument('location')
@click.option('--api-key', '-a')
def main(location, api_key):
    weather = current_weather(location, api_key)
    print(f"The weather in {location} right now: {weather}.")

@click.command()
@click.argument('location')
@click.option(
    '--api-key', '-a',
    help='your API key for the OpenWeatherMap API',
)
def main(location, api_key):
    ...

...
def main(location, api_key):
    """
    A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:

    1. London,UK

    2. Canmore

    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    """
    ...

import click
import requests

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'


def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']


@click.command()
@click.argument('location')
@click.option(
    '--api-key', '-a',
    help='your API key for the OpenWeatherMap API',
)
def main(location, api_key):
    """
    A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:
    1. London,UK
    2. Canmore
    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    """
    weather = current_weather(location, api_key)
    print(f"The weather in {location} right now: {weather}.")


if __name__ == "__main__":
    main()



