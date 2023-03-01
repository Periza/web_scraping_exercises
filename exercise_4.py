from urllib.parse import urlencode
from urllib.request import urlopen
import urllib.parse
import json
import secrets

# API endpoint url
api_url = "http://geocode.xyz"

# Adress we want to geocode
address = 'Adama Reisnera 64, Osijek, Croatia'
address_param = urllib.parse.quote(address)
print(address_param)

# API request url
url = f"{api_url}/{address_param}?json=1&auth={secrets.API_KEY}"

try:
    response = urlopen(url)
    json_data = json.loads(response.read().decode('utf-8'))
    longitude, lattitude = json_data['longt'], json_data['latt']
    print(f"Longitude: {json_data['longt']}\nLattitude: {json_data['latt']}")
except Exception as e:
    print(f"{e}")