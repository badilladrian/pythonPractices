#Write a Python program to test if a 
# given page is found or not on the server.
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

#import urllib.request
#with urllib.request.urlopen('http://python.org/') as response:
#   html = response.read()

#This is an HTTP request
import requests as request

print("FIRST WRONG URL")
"""All methods might fail. For this is better
to enclosure them in a Try Catch Block.
And displaying the error for us to know what
could be happening. """
#Try to open the URL
try:
    html = urlopen("https://abcxyz.com")
#If not possible, throw a HTTP error
except HTTPError as e:
    print("HTTP error")
#If HTTP correct but URL wrong
except URLError as e:
    print("Server not found!")
#If possible then read the file and print it
else:
    print(html.read())


#This is to create a line break between function results
space = "                     /LINE***BREAK\       "
print(space)
    
print("SECOND CORRECT URL")
#Try to open the URL
try:
    data = urlopen("http://www.example.com/")
#If not possible, throw a HTTP error
except HTTPError as e:
    print("HTTP error")
#If HTTP correct but URL wrong
except URLError as e:
    print("Server not found!")
#If possible then read the file and print it
else:     #URLOpen is an Object, which has a context manager
    print("HTML Details of "+ data.geturl()) #String of URL  
    print(data.read())  

#Another way to create line Breaks!
print("===================================================")
print("THIRD WITH HTTP REQUEST")

"""As mentioned Python has tons of packages,
request is one of them for handling HTTP requests.
Now using the request package, same less code"""
response = request.get("http://www.example.com/")

test = response.text
print("robots.txt for http://www.wikipedia.org/")

def lineBreak():
    print("====--3--============---3---=========--3--===============")

lineBreak()
print(test)
