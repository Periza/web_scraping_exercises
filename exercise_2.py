# Write a Python program to download and display the content of robot.txt for en.wikipedia.org

from urllib.request import urlopen

# url of the robots.txt file on wikipedia
url = 'http://en.wikipedia.org/robots.txt'

# get response
response = urlopen(url)
# and print it out
print(response.read().decode('utf-8'))