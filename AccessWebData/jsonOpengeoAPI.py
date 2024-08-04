#
# ? http://py4e-data.dr-chuck.net/opengeo?qAnn+Arbor%2C+MI
import urllib.request, urllib.parse, urllib.error
import json, ssl

serviceURL = 'http://py4e-data.dr-chuck.net/opengeo?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address.strip()) == 0:break
    
    address = address.strip()
    params = dict()
    params['q'] = address
    
    url = serviceURL + urllib.parse.urlencode(params)
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data),'characters', data[:27].replace('\n',' '))
    
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
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    country = js['features'][0]['properties']['country']
    print(f'Lat: {lat}\nLong: {lon}\nCountry: {country}')
    