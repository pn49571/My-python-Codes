import json
import folium
from osgeo import ogr
import webbrowser


geomcol =  ogr.Geometry(ogr.wkbGeometryCollection)
line1 = []
poly1 = []
with open('E:/En/LxCellTracker/temp.JSON') as f:
    for line in f:
        list_json = (json.loads(line))
        print(list_json)
        for x in list_json:
            for y in x:
                print(y.keys())
                if (y[u'__type']).split(",")[0] == "AwsGeometries.LineString":
                    inner_items = y[u'Vertices']
                    line = ogr.Geometry(ogr.wkbLineString)
                    for item in inner_items:
                        line.AddPoint(item[u'X'], item[u'Y'])
                        line1.append((str("(") + str(item[u'X']) + str(",") +
                                      str(item[u'Y']) + str(")")))
                    geomcol.AddGeometry(line)
                if (y[u'__type']).split(",")[0] == "AwsGeometries.Polygon":
                    inner_items = y[u'ExteriorRing'][u'Vertices']
                    ring = ogr.Geometry(ogr.wkbLinearRing)
                    for item in inner_items:
                        ring.AddPoint(item[u'X'], item[u'Y'])
                        poly1.append((str("(") + str(item[u'X']) + str(",") +
                                      str(item[u'Y']) + str(")")))
                    poly = ogr.Geometry(ogr.wkbPolygon)
                    poly.AddGeometry(ring)
                    geomcol.AddGeometry(poly)
    geojson = geomcol.ExportToJson()

#         count = 0
#         for item in list_json:
#             inner_item = item['ExteriorRing']['Vertices']
#             ring = ogr.Geometry(ogr.wkbLinearRing)
#             for inneritems in inner_item:
#                 ring.AddPoint(inneritems[u'X'], inneritems[u'Y'])
#             poly = ogr.Geometry(ogr.wkbPolygon)
#             poly.AddGeometry(ring)
#             multipolygon.AddGeometry(poly)



f = open('map.json', 'w')
print(",".join(line1))
print(",".join(poly1))
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
