'''
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
and retrieve the first plus_code from the JSON. An Open Location Code is a textual identifier that is another form of address 
based on the location of the address.
API End Points
To complete this assignment, you should use this API endpoint that has a static subset of the Open Street Map Data.
http://py4e-data.dr-chuck.net/opengeo?
This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to provide the address that you are requesting as the q= parameter that is properly URL encoded using 
the urllib.parse.urlencode() function

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a plus_code of "6FV8QPRJ+VQ".
Enter location: South Federal University
Retrieving http://...
Retrieved 1289 characters
Plus code 6FV8QPRJ+VQ

Turn In
Please run your program to find the plus_code for this location:
University of Sarajevo
Make sure to enter the name and case exactly as above and enter the plus_code and your Python code below. Hint: The first five characters 
of the plus_code are "8FMWR ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - 
but the plus_code may not match for this assignment.
'''

import urllib.request, urllib.parse, urllib.error
import json, ssl

serviceURL = 'http://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address.strip()) == 0:
        print("No address...")
        break
    
    address = address.strip()
    params = dict()
    params['q'] = address
    
    url = serviceURL + urllib.parse.urlencode(params)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data),'characters')
    
    try:
        js = json.loads(data)
    except:
        js=None
        
    if not js or 'features' not in js:
        print('== Donwload error ==')
        print(data)
        continue
    if len(js['features']) ==0 :
        print('== Location not found ==')
        print(data)
        continue
    plusCode = js['features'][0]['properties']['plus_code']
    print(f'Plus code: {plusCode}')
    