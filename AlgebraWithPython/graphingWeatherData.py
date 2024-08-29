#
# ! pip install meteostat
# * Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily # * Daily Monthly
import urllib.request, urllib.parse, urllib.error
import json, ssl

# * Documentation
# * https://dev.meteostat.net/python/daily.html#data-structure

'''
tavg	The average air temperature in °C	        Float64
tmin	The minimum air temperature in °C	        Float64
tmax	The maximum air temperature in °C	        Float64
prcp	The daily precipitation total in mm	        Float64
snow	The snow depth in mm	                    Float64
wdir	The average wind direction in degrees (°)	Float64
wspd	The average wind speed in km/h	            Float64
wpgt	The peak wind gust in km/h	                Float64
pres	The average sea-level air pressure in hPa	Float64
tsun	The daily sunshine total in minutes (m)	    Float64
'''

def get_lat_long(address):
    
    serviceURL = 'http://py4e-data.dr-chuck.net/opengeo?'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    address = address.strip()
    params = dict()
    params['q'] = address
    
    url = serviceURL + urllib.parse.urlencode(params)
        
    #print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #print('Retrieved', len(data),'characters', data[:27].replace('\n',' '))
        
    try:
        js = json.loads(data)
    except:
        js=None
            
    if not js or 'features' not in js:
        print('== Donwload error ==')
        return (None, None)
    
    if len(js['features']) ==0 :
         print('== Location not found ==')
         return (None, None)
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    country = js['features'][0]['properties']['country']
    print(f'Lat: {lat}\nLong: {lon}\nCountry: {country}')
    return (lat,lon)
    

# * Set time period
start = datetime(2024, 1, 1)
end = datetime.today()

while True:
    address = input('Enter location: ')
    if len(address.strip()) == 0:break

    # * Create Point for Fegurri SAC Peru -5.313974109599067, -80.620427026401
    lat,long = get_lat_long(address)
    if lat is None or long is None:
        continue
    else:
        philly = Point(float(lat),float(long))

        # Get daily data 
        data = Daily(philly, start, end)
        data = data.fetch()

        try:
            #for index, value in data['tmax'].items():
             #   print(f"Index: {index}, Value: {value}")
            #print((x) for x in data['tmax'])
            # Plot line chart  
            data.plot(y=['tavg', 'tmax','tmin'])
            plt.grid(True)
            plt.show()
        except:
            print('No meteorological data in this address')