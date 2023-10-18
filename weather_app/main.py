from flask import Flask
from flask import request
from flask import render_template
import pandas as pd 
import os
import folium
from folium.plugins import HeatMap, HeatMapWithTime
from datetime import date, timedelta
import sys

sys.path.append('./bin/')
import utils

app = Flask(__name__)

@app.route('/')
def draw_map():

    df = pd.read_csv('./data/three_month_data.csv')
    df['lat'] = df['lat'].apply(lambda x: x[1:])
    df['long'] = df['long'].apply(lambda x: x[:-1])
    dates = utils.get_dates(90)
    grouped = df.groupby('date')
    month_labels = [d.strftime('%B %Y') for d in pd.date_range(start=dates[0], end=dates[1])]

    heatmap_data = []
    for name, group in grouped:
        day_data = [[row['lat'], row['long'], row['temp']] for index, row in group.iterrows()]
        heatmap_data.append(day_data)

    startingLocation = [24.774265, 46.738586]
    hmap = folium.Map(location=startingLocation, zoom_start=5)
    HeatMapWithTime(heatmap_data,index=month_labels, blur=0.5, use_local_extrema=True, max_opacity=0.8).add_to(hmap)

    hmap.save(os.path.join('./static', 'heatmap.html'))
    
    cities = pd.read_json('./etc/cities.json')
    return render_template('index.html', cities = cities['cities'])

@app.route('/fetch_2_weeks_data', methods=['POST'])
def fetch_data():
    data = request.json
    city1 = data.get('city1')
    city2 = data.get('city2')
    print(city1)
    print(city2)
    context = utils.fetch_2_weeks_data(city1, city2)
    return context
if __name__ == '__main__':
    app.run(debug=True)