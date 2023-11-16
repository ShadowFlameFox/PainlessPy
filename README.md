# API-Kit Python Library
## Overview
The WeatherAPI Python library is a simple tool designed to interact with the WeatherAPI service, allowing users to retrieve weather information for a specific location.

## Features
Get the current temperature.
Retrieve the maximum temperature for the day.
Obtain the minimum temperature for the day.
Retrieve the average temperature for the day.
Installation
To use the WeatherAPI library, you need to install it using the following command:
`pip install weatherapi-library`
## Usage
### Initializing the WeatherAPI Object
```
from weatherapi_library import WeatherAPI

weatherapi_key = "YOUR_WEATHERAPI_KEY"`
location = "City, Country"`
unit = "c"  # Temperature unit, default is Celsius
weather = WeatherAPI(weatherapi_key, location, unit)
```
### Getting Current Temperature
```
current_temperature = weather.get_current_temperature()
print(f"Current Temperature: {current_temperature}°{unit.upper()}")
```
### Getting Maximum Temperature
```
max_temperature = weather.get_max_temperature()
print(f"Maximum Temperature: {max_temperature}°{unit.upper()}")
```
### Getting Minimum Temperature
```
min_temperature = weather.get_min_temperature()
print(f"Minimum Temperature: {min_temperature}°{unit.upper()}")
```
### Getting Average Temperature
```
avg_temperature = weather.get_avg_temperature()
print(f"Average Temperature: {avg_temperature}°{unit.upper()}")
```
## Dependencies
[requests](https://pypi.org/project/requests/): Used for making HTTP requests to the WeatherAPI service.
## License
This library is licensed under the [MIT License].

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests on the [GitHub repository](https://github.com/ShadowFlameFox/API-Kit/).
