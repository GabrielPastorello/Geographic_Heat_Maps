import googlemaps
import pandas as pd
import numpy as np
import time

gmaps = googlemaps.Client(key='YOUR_KEY_HERE')

# Limits of Porto Alegre
lat1 = -30.239528
lat2 = -29.956536
lng1 = -51.266669
lng2 = -51.089037

# Limits of Milan
#lat1 = 45.393802
#lat2 = 45.534424
#lng1 = 9.066306
#lng2 = 9.280889

# Limits of Timisoara
#lat1 = 45.701514
#lat2 = 45.789141
#lng1 = 21.152892
#lng2 = 21.297276

# Limits of Belgrade
#lat1 = 44.701912
#lat2 = 44.887116
#lng1 = 20.228269
#lng2 = 20.618971

num = 100 # 1/num = interval

coords = []
for lat in range(int(lat1*num), int(lat2*num)):
    for lng in range(int(lng1*num), int(lng2*num)):
        coords.append([lat/num, lng/num])

names = []
latit = []
long = []
code = []

for lat,lng in coords:
    # Search for bars within a radius of coordinates
    places = gmaps.places_nearby(location=(lat, lng),
                                radius=1000, type='bar')
    
    for place in places['results']:
        
        names.append(place['name'])
        latit.append(place['geometry']['location']['lat'])
        long.append(place['geometry']['location']['lng'])
        try:
            code.append(place['plus_code']['compound_code'])
        except:
            code.append(np.NaN)

  time.sleep(0.5)

bars = pd.DataFrame(list(zip(names,latit,long,code)),
                     columns=['NAME','LATITUDE','LONGITUDE','CODE'])

bars = bars.drop_duplicates(subset=['NAME','LATITUDE','LONGITUDE'])

bars = bars[(bars['CODE'].str.contains('Porto Alegre - RS'))|(
            bars['CODE'].isna())]

bares.to_csv(path_save+sep+'bars_Porto_Alegre.csv',
             sep=',', decimal='.',index=False,encoding='utf-8')

