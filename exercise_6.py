# Write a Python program to extract h1 tag from example.com

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://example.com'

# Make the request
response = urlopen(url)

# Get the html
content = response.read()

# Parse html
bs = BeautifulSoup(content, 'html.parser')

# Get the h1 tag
tag = bs.find('h1').text.strip()

# Print the tag
print(tag)