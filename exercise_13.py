# Write a Python program to get the number of people visiting a U.S. government website right now.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import gzip

url = 'https://analytics.usa.gov/data/live/realtime.json'

# Make a request
response = urlopen(url).read()

# Decompress the data
content = gzip.decompress(response)

# Decode data as UTF-8
data = content.decode('utf-8')

# Get the object from json data
json_data = json.loads(data)

# Print current number of visitors
print(json_data['data'][0]['active_visitors'])