#
# ? Using urllib in python
# * that does all the socket work for ys and makes web pages look like a file
# * Before scraping a website, it's crucial to ensure that the website allows scraping, 
# * typically indicated in its robots.txt file or terms of service. This helps in adhering to legal and ethical guidelines.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def openRomeo():
    fhand= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())

# TODO What is web scraping
# * when a program to be a browser a retrieves web pages, extract information
# * pip install beautifulsoup4

url = 'http://www.dr-chuck.com/page1.html'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
print(soup)
#Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))