# Write a Python program to extract and display all the image links from en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer).

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)'

# Make the request
response = urlopen(url)

# Get the html
content = response.read()

# Parse html
bs = BeautifulSoup(content, 'html.parser')

# Find all images
images = bs.find_all('img')

# Get all the urls
img_urls = [img['src'] for img in images]

# Print all the links
for url in img_urls:
    print(url)


