import json
import folium
from osgeo import ogr
import webbrowser
import glob, os
import json
import numpy as np
from folium import plugins

lons = []
lats = []
reason = []


os.chdir("C:\\Users\\SThangaraj\\Downloads\\manager-flashes")
for file in glob.glob("*.json"):
        f=open(file,'r')
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

ice_map = folium.Map(location=[38.9, -77.05], tiles='CartoDB positron', zoom_start=5)


# mark each station as a point
for i in range(0, len(lats)):
    folium.CircleMarker([lats[i], lons[i]],
                        radius=1,
                        fill_color="#3db7e4",).add_to(ice_map)

ice_map.save(outfile='map-manager.html')
webbrowser.open_new_tab('map-manager.html')
