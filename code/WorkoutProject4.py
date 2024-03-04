import json as js
from urllib import request, error
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class weatherAPI:
    def __init__(self, key):
        self.url = "https://api.weatherbit.io/v2.0"
        self.api_key = key


    def get_curr_weather(self, city):
        url = f"{self.url}/current"
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
    plt.figure(figsize=(8, 6))

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temperature over Time')
    with PdfPages('weather_visualization.pdf') as pdf:
        pdf.savefig()
        plt.close()


def start():
    key = "53d3ac0dbfab4f74bf59d721b484fd05"
    curr_weather = weatherAPI(key)
    city = "Oakland"
    curr_weather_data = curr_weather.get_curr_weather(city)
    write_to_json(curr_weather_data, "current weather.json")





if __name__ == "__main__":
    start()