# Write a Python program to that retrieves an arbitary Wikipedia page of "Python" and creates a list of links on that page.

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/Python'

# Make a request
html = urlopen(url)

# Get the html
response = html.read()

# Parse html
bs = BeautifulSoup(response)

# Print links
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

