# Write a Python program to get 90 days of visits broken down by browser for all sites on data.gov.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import gzip

url = 'https://analytics.usa.gov/data/live/browsers.json'

req = urlopen(url)

# We get the data that is compressed, so we have to decompress it
data = gzip.decompress(req.read())

# Decode the data as UTF-8
response = data.decode('utf-8')

# Get the json data
json_data = json.loads(response)

# Print the used browsers
print(json_data['totals']['browser'])









