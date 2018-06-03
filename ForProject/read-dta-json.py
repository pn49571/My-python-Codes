import json
import folium
from osgeo import ogr
import webbrowser

multipolygon = ogr.Geometry(ogr.wkbMultiPolygon)

with open('E:/En/LxCellTracker/ExportLocal/LatestAllWarningBoxes.JSON') as f:
    for line in f:
        list_json = (json.loads(line))
        count = 0
        for item in list_json:
            inner_item = item['ExteriorRing']['Vertices']
            ring = ogr.Geometry(ogr.wkbLinearRing)
            for inneritems in inner_item:
                #print (inneritems[u'X'], inneritems[u'Y'])
                ring.AddPoint(inneritems[u'X'], inneritems[u'Y'])

                #print(inner_item['Y'], inneritems['X'])
            # for key, value in item.items():
            #     print(key)
            #     #print("item{}: {}".format(count, item))
            poly = ogr.Geometry(ogr.wkbPolygon)
            poly.AddGeometry(ring)
            multipolygon.AddGeometry(poly)
    geojson = multipolygon.ExportToJson()

f = open('map.json', 'w')

f.write(geojson)
f.close()

geo_path = r'map.json'

ice_map = folium.Map(location=[-59.1759, -11.6016],
                     tiles='Mapbox Bright', zoom_start=5)

ice_map.choropleth(geo_data=geo_path,
                   fill_color='YlGn',
                   fill_opacity=0.7, line_opacity=0.2,)
ice_map.save(outfile='map.html')
webbrowser.open_new_tab('map.html')
