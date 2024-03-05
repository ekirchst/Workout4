# Evan Kirchstetter
# ekirchst@uci.edu
# 59946460
import json as js
from urllib import request


class weatherAPI:
    '''
    Weather API Class Created to Interact with Weatherbit api
    '''
    def __init__(self, key):
        '''
        Initializes WeatherAPI Object
        Takes in key
        '''
        self.url = "https://api.weatherbit.io/v2.0"
        self.api_key = key

    def get_daily_weather(self, city):
        '''
        Function to Connect to weatherapi.io with daily weather specified
        returns json data
        '''
        url = f"{self.url}/forecast/daily"
        params = {
            "key": self.api_key,
            "city": city
        }
        full = f"{url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
        response = request.urlopen(full)
        re = js.loads(response.read())
        print(re)
        return re


def write_to_json(data, filename):
    '''
    Creates json File with Output Data From Weather api
    Incredibly Easy to Read
    '''
    with open(filename, "w") as file:
        js.dump(data, file)