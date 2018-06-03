import folium
from osgeo import ogr
import webbrowser

multipolygon = ogr.Geometry(ogr.wkbMultiPolygon)

# Create test polygon
ring1 = ogr.Geometry(ogr.wkbLinearRing)
ring1.AddPoint(-10.92, 8.84)
ring1.AddPoint(-10.67,8.16)
ring1.AddPoint(-10.99,8.1)
ring1.AddPoint(-11.02, 8.82)
#ring.AddPoint(1218405.0658121984, 721108.1805541387)
#ring.AddPoint(1179091.1646903288, 712782.8838459781)
poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring1)

multipolygon.AddGeometry(poly)

ring2 = ogr.Geometry(ogr.wkbLinearRing)
ring2.AddPoint(-11.24, 8.88)
ring2.AddPoint(-11.38, 9.47)
ring2.AddPoint(-11.04, 9.5)
ring2.AddPoint(-11.07, 8.9)

poly = ogr.Geometry(ogr.wkbPolygon)
poly.AddGeometry(ring2)

multipolygon.AddGeometry(poly)

#geojson = poly.ExportToJson()
geojson = multipolygon.ExportToJson()
print geojson
#print wkt
f = open('map.json','w')

f.write(geojson)
f.close()

geo_path = r'map.json'

ice_map = folium.Map(location=[-59.1759, -11.6016],
                     tiles='Mapbox Bright', zoom_start=2)

ice_map.choropleth(geo_data=geo_path)
ice_map.save(outfile='map.html')
webbrowser.open_new_tab('map.html')
# os.remove('map.html')
print ice_map
