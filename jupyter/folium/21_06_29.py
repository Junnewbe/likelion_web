# -*- coding: utf-8 -*-
"""21_06_29.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_tGdLZbxmVUMamKXYw2P2DZYZyMf_h_z
"""

# 위도(latitude), 경도(longitude) 를 이용한 위치표시
import folium
loc = folium.Map(location=[37.551777, 126.924964],zoom_start=15)
# loc

loc.save("map.html")

import os
path = os.getcwd()
os.listdir(path)

# 37.5510887807618, 126.94101302634627
loc=folium.Map(location=[37.5510887807618, 126.94101302634627],
               zoom_start=15)
folium.Marker([37.5510887807618, 126.94101302634627]).add_to(loc)
folium.Marker([37.5493866956154, 126.93933040409388]).add_to(loc)
loc

m = folium.Map(
location=[37.5466423,126.9092281],
zoom_start=15
)
folium.Marker(
location=[37.5466423,126.9092281],
popup = 'yanghwajin', # 선택 시 popup
icon = folium.Icon(color='purple', icon="info-sign") # 아이콘 # glyphicon-check, star
).add_to(m)
folium.Marker(
location=[37.5510887807618, 126.941013026346271],
popup = 'Seogang_Uni', # 선택 시 popup
icon = folium.Icon(color='blue', icon="info-sign") # 아이콘 # glyphicon-check, star
).add_to(m)
m

m = folium.Map(
location=[36.33989545027838, 128.15641529898116],
zoom_start=4
)
folium.Marker(
location=[5.396325116479463, 100.26407533428355],
popup = 'Penang', # 선택 시 popup
icon = folium.Icon(color='red', icon="info-sign") # 아이콘 # glyphicon-check, star
).add_to(m)
folium.Marker(
location=[12.672886045507807, 105.1088825311528],
popup = 'Cambodia', # 선택 시 popup
icon = folium.Icon(color='blue', icon="info-sign") # 아이콘 # glyphicon-check, star
).add_to(m)
folium.Marker(
location=[43.08292456109717, -79.074168704936438],
popup = 'Niagara', # 선택 시 popup
icon = folium.Icon(color='purple', icon="info-sign") # 아이콘 # glyphicon-check, star
).add_to(m)
folium.Marker(
location=[42.4799343157859, -83.47569061543611],
popup = 'Sis_house', # 선택 시 popup
icon = folium.Icon(color='green', icon="info-sign") # 아이콘 # glyphicon-check, star
).add_to(m)
folium.Marker(
location=[37.64406396564595, 126.66725628892885],
tooltip = '우 리 집', # 선택 시 popup
icon = folium.Icon(color='green', icon="info-sign") # 아이콘 # glyphicon-check, star
).add_to(m)
m

folium.CircleMarker(
location=[42.52382372071403, -83.51044545534144],
radius=100,
color = '#ffffgg',
fill_color='#fffggg',
popup = 'Sis_house', # 선택 시 popup
).add_to(m)
m

m = folium.Map(
    location=[37.5466423,126.9092281],
    zoom_start=15
)
folium.CircleMarker(
    location=[37.5466423,126.9092281],
    radius = 100,
    color = '#ffffgg',
    fill_color='#fffggg',
    popup = 'yanghwajin',                         # 선택 시 popup
).add_to(m)
m

from folium import plugins
import numpy as np
import os

N=50
data=np.array(
    [
     np.random.uniform(low=37.4, high=37.6, size=N),
     np.random.uniform(low=127.1, high=126.8, size=N)
    ]
).T
print(data[0:10])

popups = [str(i) for i in range(N)] # Popups texts are simple numbers.
m = folium.Map([37.558330274882586, 126.9878095271063], zoom_start=4)
plugins.MarkerCluster(data, popups=popups).add_to(m)
m.save(os.path.join('.', 'Plugins_1.html'))
m

# shift+tab 누르면 함수 사용여부 확인 가능!

import folium
m = folium.Map(
location=[37.5838699,127.0565831],
zoom_start=10
)

import json
with open('seoul_muncipalities_geo.json',mode='rt',encoding='utf-8') as f:
  geo = json.loads(f.read())
  f.close()
folium.GeoJson(
geo,
name='seoul_municipalities'
).add_to(m)
m.save('map.html')
m

stamen = folium.Map(location=[45.5236, -122.6750],
                    tiles='Stamen Toner', 
                    zoom_start=13)
stamen

stamen = folium.Map(location=[45.5236, -122.6750],
                    tiles='Stamen Terrain', 
                    zoom_start=13)
stamen

import folium
from folium import Marker, Icon
import pandas as pd
import csv, time

jeju= pd.read_csv('./jeju.csv', encoding='cp949')
jeju.head()

df_sample = jeju[['카메라대수','위도','경도']]
# display(df_sample.head(3))
print('데이터 널값 확인')
display(df_sample.isnull().sum())

loc=[33.37860539157057, 126.52645770837371]
map = folium.Map(loc,   tiles='Stamen Terrain', zoom_start=11)
for i in range(len(jeju)):
  folium.Marker(location=[jeju.loc[i]['위도'],jeju.loc[i]['경도']],
                tooltip=jeju.loc[i]['카메라대수'],
                icon = folium.Icon(color='green', icon="info-sign")
                ).add_to(map)
map.save('jeju.html')
map