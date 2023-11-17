import requests
import json

class WeatherAPI:
    def __init__(self, weatherapi_key, location):
        self.key = weatherapi_key
        self.location = location

    def get_current_temperature(self, unit = "c"):
        self.unit = unit
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['current'][f'temp_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_max_temperature(self, unit = "c"):
        self.unit = unit
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'maxtemp_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_min_temperature(self, unit = "c"):
        self.unit = unit
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'mintemp_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_avg_temperature(self, unit = "c"):
        self.unit = unit
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'avgtemp_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_max_wind_speed(self, unit = "kph"):
        self.unit = unit
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'maxwind_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_total_precipitation(self, unit = "mm"):
        self.unit = unit
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'totalprecip_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_wind_direction(self, format = "dir"):
        self.format = format
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['current'][f'wind_{self.format}']
        else:
            raise Exception(self.data['error']["message"])
            

class BetterJSON:
    def __init__(self):
        pass

    def load_data(self, file):
        try:
            with open(f"{file}", "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return {}

    def save_data(self, file, data):
        with open(f"{file}", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def update_object(self, file, object, new_value):
        data = self.load_data(file)
        data[object] = new_value
        self.save_data(data, file)

    def get_object(self, file, object):
        data = self.load_data(file)
        try:
            return data[object]
        except KeyError:
            return None

if __name__ == "__main__":
    pass