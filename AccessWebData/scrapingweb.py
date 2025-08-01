#
# ? exercise
'''
Scraping Numbers from HTML using BeautifulSoup 
The program will use urllib to read the HTML from the data files below, and parse the data, 
extracting numbers and compute the sum of the numbers in the file.

We provide the file for this assignment.
Actual data: http://py4e-data.dr-chuck.net/comments_2066179.html (Sum ends with 6)

You do not need to save these files to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like 
the following:
    <tr><td>Modu</td><td><span class="comments">90</span></td></tr>
    <tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
    <tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
    
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.

for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url ='http://py4e-data.dr-chuck.net/comments_2066179.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
spans = soup('span')
print(sum([int(span.contents[0]) for span in spans]))




