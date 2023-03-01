# Write a Python program to test if a given page is found or not on the server.

from urllib.request import urlopen

# We are going to check if we get HTTPError with status 404
# when we send a GET request to the server
from urllib.error import HTTPError

def testPage(url):
    try:
        response = urlopen(url)
        print("The page was found")
    except HTTPError as e:
        print(f"{e.code}: The page could not be found.")

# Testing the function
testPage("http://www.google.hr") # The page was found
testPage("http://www.google.hr/kittens") # 404: The page could not be found.
