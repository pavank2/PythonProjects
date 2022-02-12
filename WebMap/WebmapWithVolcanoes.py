import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
  if elevation < 1500:
      return 'green'
  elif 1500 <= elevation > 2000:
      return 'orange'
  else:
      return 'red'          


html = """ <h4>Volcano Information:<h4>
Height: %s m
"""

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")


fg=folium.FeatureGroup(name="My Map")
for lt,ln,elev in zip(lat,lon,elev):
    iframe = folium.IFrame(html = html % str(elev), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=folium.Popup(iframe),radius=20,fill=True,fill_color=color_producer(elev)))

fg.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000
else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red' }))

map.add_child(fg)
map.save("WebMap.html")