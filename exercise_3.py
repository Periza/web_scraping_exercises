# Write a Python program to get the number of datasets currently listed on data.gov

from urllib.request import urlopen

# beautiful soup library
from bs4 import BeautifulSoup

url = 'http://www.data.gov'
response = urlopen(url)

bs = BeautifulSoup(response, 'html.parser')

# what we are searching for is inside a tag that is inside small tag
content = bs.select_one('small a').text.strip()
print(f"Number of datasets listed: {content}")