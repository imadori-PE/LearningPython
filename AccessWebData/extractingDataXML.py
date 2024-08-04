'''
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.
Actual data: http://py4e-data.dr-chuck.net/comments_2066181.xml (Sum ends with 28)
You do not need to save the file to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:
<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
You are to look through all the <comment> tags and find the <count> values sum the numbers. 
To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the 
following line of code:
counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. 
You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET  

url='http://py4e-data.dr-chuck.net/comments_2066181.xml'
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)
nodes=tree.findall('.//count')
print(sum([int(node.text) for node in nodes]))