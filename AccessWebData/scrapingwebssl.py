import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import site
import sys

# * Python Global Environment: To see the exact path on your system, you can use the following Python command:
print(site.getsitepackages())
# * Virtual environment (venv or virtualenv):
print(sys.path)

# ? example with SSL certificate 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# test with https://www.dr-chuck.com/
url = input('Enter URL: ' )
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

print(soup)

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
    