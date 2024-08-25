#
# ! pip install meteostat
# * Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily # * Daily Monthly

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

# * Set time period
start = datetime(2024, 1, 1)
end = datetime.today()

# * Create Point for Fegurri SAC Peru -5.313974109599067, -80.620427026401
philly = Point(-5.313974109599067,-80.620427026401)

# Get daily data 
data = Daily(philly, start, end)
data = data.fetch()

for index, value in data['tmax'].items():
    print(f"Index: {index}, Value: {value}")
#print((x) for x in data['tmax'])
# Plot line chart 
data.plot(y=['tavg', 'tmax','tmin'])
plt.grid(True)
plt.show()