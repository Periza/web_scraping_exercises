# Write a Python program to extract and display all the header tags from en.wikipedia.org/wiki/Main_Page.

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://en.wikipedia.org/wiki/Main_Page'

# Make the request
response = urlopen(url)

# Get the thml
content = response.read()

# Parse html
bs = BeautifulSoup(content, 'html.parser')

# Get all tags
header_tags = [bs.find_all(f"h{i}") for i in range(1, 7)]

# Print all tags
for header_list in header_tags:
    for header in header_list:
        print(header.text.strip())

