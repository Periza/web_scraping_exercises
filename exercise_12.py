# Write a Python program to list all language names and number of related articles in the order they appear in wikipedia.org.

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.wikipedia.org/'

# Make a request
content = urlopen(url)

# Parse the content
bs = BeautifulSoup(content, features='html.parser')

names = bs.find_all('a', {'class': 'link-box'})

for name in names:
    print(name.text)