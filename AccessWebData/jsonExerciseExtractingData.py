'''
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts 
from the JSON data, compute the sum of the numbers in the file and enter the sum below:
Actual data: http://py4e-data.dr-chuck.net/comments_2066182.json (Sum ends with 41)
You do not need to save the file to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The data consists of a number of names and comment counts in JSON as follows:
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at xml3.py to see how to prompt for a URL and retrieve data from a URL.
'''
import urllib.request, urllib.parse, urllib.error
import json
url = 'http://py4e-data.dr-chuck.net/comments_2066182.json'
content = urllib.request.urlopen(url)
data = content.read().decode()
js = json.loads(data)
print( sum([(int(item['count'])) for item in js['comments']]) )

