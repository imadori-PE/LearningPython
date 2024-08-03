'''
Following Links in Python
The program will use urllib to read the HTML from the data files below, extract the href= values from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat 
the process a number of times and report the last name you find.
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Joshiah.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: K
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to do the assignment without 
writing a Python program. But frankly with a little effort and patience you can overcome these attempts to make it a little harder to complete 
the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def getHref(url,pos):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    anchorTags = soup('a') 
    return ( anchorTags[pos].get('href', None) , anchorTags[pos].contents[0] ) 


newURL ='http://py4e-data.dr-chuck.net/known_by_Joshiah.html'
position=18
repeat=1
while repeat<=7:
    (newURL,lastName)=getHref(newURL,position-1)
    repeat=repeat+1
print(lastName)