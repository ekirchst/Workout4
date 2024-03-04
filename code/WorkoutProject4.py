import json as js
from urllib import request, error
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class weatherAPI:
    def __init__(self, key):
        self.url = "https://api.weatherbit.io/v2.0"
        self.api_key = key


    def get_daily_weather(self, city):
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
    with open(filename, "w") as file:
        js.dump(data, file)


def visualize_weather(data):
    dates = [entry['datetime'] for entry in data['data']]
    high_temps = [entry['high_temp'] for entry in data['data']]
    low_temps = [entry['low_temp'] for entry in data['data']]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, high_temps, marker='o', linestyle='-', label='High Temp')
    plt.plot(dates, low_temps, marker='o', linestyle='-', label='Low Temp')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily High and Low Temperatures')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
    with PdfPages('weather_visualization.pdf') as pdf:
        pdf.savefig()
        plt.close()


def start():
    key = "53d3ac0dbfab4f74bf59d721b484fd05"
    daily_weather = weatherAPI(key)
    city = "Oakland"
    daily_weather_data = daily_weather.get_daily_weather(city)
    write_to_json(daily_weather_data, "current weather.json")
    visualize_weather(daily_weather_data)





if __name__ == "__main__":
    start()