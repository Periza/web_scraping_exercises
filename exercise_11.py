# Write a Python program to check whether a page contains a title or not.

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bs = BeautifulSoup(html.read(), features='html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    
    return title

    title = getTitle(url)
    if title == None:
        return "Title could not be found"
    else:
        return title

print(getTitle("https://www.w3resource.com"))
print(getTitle("http://www.example.com/"))

