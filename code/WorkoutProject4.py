# Evan Kirchstetter
# ekirchst@uci.edu
# 59946460
import API as api
from Visualize import visualize_weather


def start():
    '''
    Start Function
    Assigns values to variables, Creates WeatherAPI object, and calls functions
    '''
    key = "53d3ac0dbfab4f74bf59d721b484fd05"
    daily_weather = api.weatherAPI(key)
    city = input("Enter City (with no spaces)")
    daily_weather_data = daily_weather.get_daily_weather(city)
    api.easy_to_read(daily_weather_data, "daily weather read file.json")
    visualize_weather(daily_weather_data)


if __name__ == "__main__":
    '''
    Function to start code when file is run
    '''
    start()
