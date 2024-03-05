# Evan Kirchstetter
# ekirchst@uci.edu
# 59946460
from API import write_to_json, weatherAPI
from Visualize import visualize_weather


def start():
    key = "53d3ac0dbfab4f74bf59d721b484fd05"
    daily_weather = weatherAPI(key)
    city = "NewYork"
    daily_weather_data = daily_weather.get_daily_weather(city)
    write_to_json(daily_weather_data, "current weather.json")
    visualize_weather(daily_weather_data)


if __name__ == "__main__":
    start()
