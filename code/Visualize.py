# Evan Kirchstetter
# ekirchst@uci.edu
# 59946460
import matplotlib.pyplot as plt


def visualize_weather(data):
    '''
    Function Creating a Visual Plot of Data Retrieved with Labels
    '''
    dates = [entry['datetime'] for entry in data['data']]
    high_temps = [entry['high_temp'] for entry in data['data']]
    low_temps = [entry['low_temp'] for entry in data['data']]
    city_name = data['city_name']
    plt.figure(figsize=(10, 6)) 
    plt.plot(dates, high_temps, marker='o', linestyle='-', label='High Temp')
    plt.plot(dates, low_temps, marker='o', linestyle='-', label='Low Temp')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Daily High and Low Temperatures in {city_name}')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('WorkoutProject4-59946460.jpg')
