import requests

class WeatherAPI:
    def __init__(self, weatherapi_key:str, location:str):
        self.key = weatherapi_key
        self.location = location

    def get_current_temperature(self, unit = "c"):
        """
        c = Temperature in celsius.\n
        f = Temperature in fahrenheit.
        """
        self.unit = unit
        if self.unit not in ["c", "f"]:
            raise Exception("Invalid unit.")
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['current'][f'temp_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_max_temperature(self, unit = "c"):
        """
        c = Temperature in celsius.\n
        f = Temperature in fahrenheit.
        """
        self.unit = unit
        if self.unit not in ["c", "f"]:
            raise Exception("Invalid unit.")
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'maxtemp_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_min_temperature(self, unit = "c"):
        """
        c = Temperature in celsius.\n
        f = Temperature in fahrenheit.
        """
        self.unit = unit
        if self.unit not in ["c", "f"]:
            raise Exception("Invalid unit.")
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'mintemp_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_avg_temperature(self, unit = "c"):
        """
        c = Temperature in celsius.\n
        f = Temperature in fahrenheit.
        """
        self.unit = unit
        if self.unit not in ["c", "f"]:
            raise Exception("Invalid unit.")
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'avgtemp_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_max_wind_speed(self, unit = "kph"):
        """
        kph = Maximum wind speed in kilometer per hour.\n
        mph = Maximum wind speed in miles per hour.
        """
        self.unit = unit
        if self.unit not in ["kph", "mph"]:
            raise Exception("Invalid unit.")
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'maxwind_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_total_precipitation(self, unit = "mm"):
        """
        mm = Precipitation amount in millimeters.\n
        in = Precipitation amount in inches.
        """
        self.unit = unit
        if self.unit not in ["mm", "in"]:
            raise Exception("Invalid unit.")
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['forecast']['forecastday'][0]['day'][f'totalprecip_{self.unit}']
        else:
            raise Exception(self.data['error']["message"])
        
    def get_wind_direction(self, format = "dir"):
        """
        dir = Wind direction as 16 point compass. e.g.: NSW\n
        degree = Wind direction in degrees.
        """
        self.format = format
        if self.format not in ["dir", "degree"]:
            raise Exception("Invalid unit.")
        self.url = f'https://api.weatherapi.com/v1/forecast.json?key={self.key}&q={self.location}&days=1'
        self.response = requests.get(self.url)

        self.data = self.response.json()

        if self.response.status_code == 200:
            return self.data['current'][f'wind_{self.format}']
        else:
            raise Exception(self.data['error']["message"])