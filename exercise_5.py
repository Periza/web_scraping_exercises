# Write a Python program to display the name of the most recently added dataset on data.gov.

from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup

base_url = 'http://catalog.data.gov/dataset'

# Encode the paremeters
params = {
    'q': '',
    'sort': 'metadata_created desc',
    'page': '1'
}

# Encode the paramateres
query_string = urlencode(params)

full_url = f"{base_url}?{query_string}"

# Make the request
response = urlopen(full_url)

# Get the content
content = response.read()

# Parse HTML
bs = BeautifulSoup(content, 'html.parser')

# Find the most recent title
title = bs.find('h3', {'class': 'dataset-heading'}).find('a').text.strip()

print(title)