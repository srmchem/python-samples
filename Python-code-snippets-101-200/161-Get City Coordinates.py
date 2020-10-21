"""
Python code snippets vol 33:
161-Get city coordinates
stevepython.wordpress.com

Source:
https://pbaumgarten.com/python/requests.html
"""
import json
import requests

def get_city_coordinates(location):
    """Get info from geocode.xyz"""

    url = "https://geocode.xyz/"+location+"?json=1"
    params = {}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        print("*** ERROR! Response ", response.status_code, " ***")
        return None

city = input("Type the name of a city: ")
info = get_city_coordinates(city)
print("City:      ", info["standard"]["city"])
print("Country:   ", info["standard"]["countryname"])
print("Latitude:  ", info["latt"])
print("Longitude: ", info["longt"])
