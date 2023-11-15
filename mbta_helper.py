# Your API KEYS (you need to use your own keys - very long random characters)
from config import MAPBOX_TOKEN, MBTA_API_KEY, OPEN_WEATHER_API
import urllib.request
import json
from pprint import pprint
import mbta_helper

# Useful URLs (you need to add the appropriate parameters for your requests)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# # A little bit of scaffolding if you want to use it
# def get_json(url: str) -> dict:
#     """
#     Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

#     Both get_lat_long() and get_nearest_station() might need to use this function.

#     """
# pass

# In this function, we retreiw tha latitude and longitude coordinates of a specificed place using the mapbox API.
# The function takes a place, queries the mapbox API, and extracs the lat and long associated with the place, returning them as a tuple


def get_lat_long(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    place_name_formatted = place_name.replace(' ', '%20')
    url = f'{MAPBOX_BASE_URL}/{place_name_formatted}.json?access_token={MAPBOX_TOKEN}&types=poi'

    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode('utf-8')
        response_data = json.loads(response_text)

    latitude, longitude = response_data['features'][0]['center']
    return latitude, longitude

# In the "Get_Nearest_Station" function, we are taking in the lat and long as trings, constructing a URL ("MBTA_URL") and sendin a request to the MBTA API to fetch information about the nearest stations based on the provided coordinates
# From the resonse data, we extract the name of the nearest station and its wheeelchair accesibility info
# Station name and wheelchair_accessible is returned as a response

def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    mbta_url = f"{MBTA_BASE_URL}?filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance&api_key={MBTA_API_KEY}"
    #print(mbta_url)

    with urllib.request.urlopen(mbta_url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)
        station_name = response_data['data'][0]['attributes']['name']
        wheelchair_accessible = response_data['data'][0]['attributes']['wheelchair_boarding'] 
        return station_name, wheelchair_accessible
    
# In this function, we are utilizing the openweather API to retrieve te current temparature of a specificed location
def get_temp(place_name):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={place_name},us&APPID={OPEN_WEATHER_API}&units=metric'
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        
        response_data = json.loads(response_text)

    return response_data['main']['temp']

# This next function interacts with the openweather API and fetches weather data based on a provided place name. 
# It encodes the place name for safe URL usage, constructs the URL with the necessary API parameters, and retrieves weather-related information from the API response.

def get_temp(place_name):
    encoded_place_name = urllib.parse.quote(place_name)
    url = f'https://api.openweathermap.org/data/2.5/weather?q={encoded_place_name},us&APPID={OPEN_WEATHER_API}&units=metric'

    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode('utf-8')
        response_data = json.loads(response_text)

    return response_data['main']['temp']

# In th e followig functions, we request for user input, and utilizing the "get_lat_long()" function to retrieve coordinates of the provided place
# The code uses these coordinates to find the nearest station with "get_nearest_station()" and obtains if the Wheelchair is accessible using binary
# Finally, for the "WOW FACTOR", we used a OpenWeather API to provide current weather at the location entered"
# All of this is printed in a list with f string formatting to make it look neat for the end user"
def main():
    """
    Test all the functions here
    """
    place_name = input("Please provide a name of a place or a valid address: ")
    longitude, latitude = get_lat_long(place_name)
    station_info = get_nearest_station(latitude, longitude)
    temperature = get_temp(place_name)

    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")
    print(f"Location: {place_name}")
    print(f"Nearest Station: {station_info[0]}")
    print(f"Wheelchair Accessible: {station_info[1]}")
    print(f"Weather Temperature: {temperature} °C")

if __name__ == '__main__':
    main()
    
