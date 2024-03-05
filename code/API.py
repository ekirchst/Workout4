# Evan Kirchstetter
# ekirchst@uci.edu
# 59946460
import json as js
from urllib import request
from WorkoutProject4 import start


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
    try:
        def get_daily_weather(self, city):
            '''
            Function to Connect to weatherapi.io with daily weather specified
            returns json data
            '''
            if ' ' in city:
                print("PLEASE ENTER A CITY WITH NO SPACES")
                start()
            url = f"{self.url}/forecast/daily"
            params = {
                "key": self.api_key,
                "city": city
            }
            temp = '&'.join([f'{key}={val}' for key, val in params.items()])
            full = f"{url}?{temp}"
            response = request.urlopen(full)
            re = js.loads(response.read())
            print(re)
            return re
    except Exception as e:
        print(f"Error: {e}")


def easy_to_read(data, filename):
    '''
    Creates json File with Output Data From Weather api
    Incredibly Easy to Read
    '''
    with open(filename, "w") as file:
        js.dump(data, file)
