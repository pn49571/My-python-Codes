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


os.chdir("XXXXXXXXXXXXXXXXXXXXXXX")
for file in glob.glob("*.json"):
        f=open(file,'r')
        for line in f:
                try:
                    decoded = json.loads(line)
                    l = decoded['portions']
                    for item1 in l:
                            reason.append(item1['XXXXXXXXXXXXXX'])
                            lons.append(item1['longitude'])
                            lats.append(item1['latitude'])
                except ValueError:
                        print("File problem")
        print(len(lats))
        f.close()
        break

ice_map = folium.Map(location=[-59.1759, -11.6016],
                     tiles='Mapbox Bright', zoom_start=5)

# mark each station as a point
for i in range(0, len(lats)):
    folium.CircleMarker([lats[i], lons[i]],
                        radius=15,
                        popup=reason[i],
                        fill_color="#3db7e4",).add_to(ice_map)

# convert to (n, 2) nd-array format for heatmap
stationArr = np.array([lats, lons]).as_matrix()

# plot heatmap
ice_map.add_children(plugins.HeatMap(stationArr, radius=15))
ice_map.save(outfile='map.html')
webbrowser.open_new_tab('map.html')
