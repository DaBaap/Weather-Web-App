# Weather-Web-App

## Introduction
This is a weather web application developed in Flask Framework. The web-app shows the line chart for any two cities in KSA for past 2 weeks. In addition to that, Heat Map is also displayed based on 3 month max temperatues per day. 

## Methodology
A weather API, provided by [https://www.visualcrossing.com](https://www.visualcrossing.com), was used to collect the 3 months data. The script is in [/bin/load_heatmap.py](https://github.com/DaBaap/Weather-Web-App/blob/main/weather_app/bin/load_heatmap.py). A python library, Folium, was used to create the heatmap and its [html file](https://github.com/DaBaap/Weather-Web-App/blob/main/weather_app/static/heatmap.html) is saved in static folder. For developing line charts, javascript library Highcharts was used. 

## Usage
1. Install the [req.txt](https://github.com/DaBaap/Weather-Web-App/blob/main/req.txt) file:
    ```pip install -r req.txt```

2. Run the [main](https://github.com/DaBaap/Weather-Web-App/blob/main/weather_app/main.py) script.
3. Select any 2 cites and click fetch button to fetch 2 weeks past data.
4. The heatmap is already shown a csv file in [data](https://github.com/DaBaap/Weather-Web-App/tree/main/weather_app/data) folder.

## Limitations
For heatmap only cities 
> ["Dammam","Jeddah","Al-Saih","Khaybar","Madinah","Mecca","Riyadh"].

are selected due to cap in API calling. The cap is [1000 records/day](https://www.visualcrossing.com/weather-data-editions) in free addition. Therefore, only 7 cities were chosen for 3 months since 7*90(90 days in 3 months) is 630 and rest of records were left for developing line charts (since they are dynamic) and for testing. However, the heatmap is dynamic and can adapt for more data points/cordinates. 
