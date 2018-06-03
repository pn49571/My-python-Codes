import folium
import pandas
import webbrowser
import os

map_hooray = folium.Map(location=[51.5074, 0.1278],
                    zoom_start = 11)
html_string = map_hooray._repr_html_()
#print html_string

f = open('map.html','w')

f.write(html_string)
f.close()
