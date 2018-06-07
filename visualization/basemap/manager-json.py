import glob, os
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from collections import Counter
from pylab import rcParams
from datetime import datetime
import io


def produceMap(lat,lon):
	fig = plt.figure(figsize=(15, 15), edgecolor='w')
	print('basemap')
	map = Basemap(projection='merc',resolution='l',
              	llcrnrlon=-180, llcrnrlat=-60,
              	urcrnrlon=180, urcrnrlat=70)
	map.fillcontinents(color="#FFDDCC",lake_color='#FFDDCC')
	map.drawmapboundary(fill_color="#DDEEFF")
	xbuddy, ybuddy = map(lat, lon)
	map.plot(xbuddy, ybuddy, '*', markersize=5,color='red')
	plt.title("LXmanager output")
	plt.savefig('lxmanager.png',bbox_inches='tight')


lons = []
lats = []

os.chdir("C:\\Users\\SThangaraj\\Documents\\Flashes\\")
for file in glob.glob("*.json"):
	print(file)
	f = open(file,'r')
	for line in f:
            try:
                decoded = json.loads(line)
                l = decoded['portions']
                for item1 in l:
                        lons.append(item1['longitude'])
                        lats.append(item1['latitude'])
            except ValueError:
                    print("File problem")
    print(len(lats))
    f.close()
    break
	#produceMap(lats,lons,reason)
	#print(decoded['portions'][0]['ACriteria'])
produceMap(lats,lons)
