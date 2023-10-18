from geopy.geocoders import Nominatim
import requests
import pandas as pd
from datetime import datetime, timedelta

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def fetch_data(city):
    three_months_dates = get_dates(90)
    start_date =  three_months_dates[0]
    end_date = three_months_dates[1]

    city_cordinates =  get_coordinates(city)

    if city_cordinates:
        city1_API_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_cordinates[0]}%2C%20{city_cordinates[1]}/{start_date}/{end_date}?unitGroup=metric&include=days&key=XNYU2JNQR5HQL94N76S7BEPSJ&contentType=csv"
    else:
        return pd.DataFrame()
    response = requests.request("GET", city1_API_url)
    if response.status_code!=200:
        print('Unexpected Status code: ', response.status_code)
    data = pd.DataFrame([response.text.splitlines()[i].split(',')[:4] for i in range(1, len(response.text.splitlines()))], columns=response.text.splitlines()[0].split(',')[:4])        
    return data

def fetch_2_weeks_data(city1, city2):

    two_week_dates = get_dates(14)

    start_date =  two_week_dates[0]
    end_date = two_week_dates[1]

    city1_cordinates =  get_coordinates(city1)
    city2_cordinates =  get_coordinates(city2)
    if city1_cordinates and city2_cordinates:
        city1_API_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city1_cordinates[0]}%2C%20{city1_cordinates[1]}/{start_date}/{end_date}?unitGroup=metric&include=days&key=XNYU2JNQR5HQL94N76S7BEPSJ&contentType=csv"
        city2_API_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city2_cordinates[0]}%2C%20{city2_cordinates[1]}/{start_date}/{end_date}?unitGroup=metric&include=days&key=XNYU2JNQR5HQL94N76S7BEPSJ&contentType=csv"
    else:
        return {'date_range': [], 
               'city1_data': [],
               'city2_data': [],
               'city1_name': [],
               'city2_name': [],
               }
    city1_response = requests.request("GET", city1_API_url)
    if city1_response.status_code!=200:
        print(city1_API_url)
        print(city2_API_url)
        print('Unexpected Status code: ', city1_response.status_code)
        return {'date_range': [], 
               'city1_data': [],
               'city2_data': [],
               'city1_name': [],
               'city2_name': [],
               }
    
    city2_response = requests.request("GET", city2_API_url)
    if city2_response.status_code!=200:
        print(city1_API_url)
        print(city2_API_url)
        print('Unexpected Status code: ', city2_response.status_code)
        return {'date_range': [], 
               'city1_data': [],
               'city2_data': [],
               'city1_name': [],
               'city2_name': [],
               }
    city1_data = pd.DataFrame([city1_response.text.splitlines()[i].split(',')[:4] for i in range(1, len(city1_response.text.splitlines()))], columns=city1_response.text.splitlines()[0].split(',')[:4])        
    city2_data = pd.DataFrame([city2_response.text.splitlines()[i].split(',')[:4] for i in range(1, len(city2_response.text.splitlines()))], columns=city2_response.text.splitlines()[0].split(',')[:4])

    week_dates = city1_data.iloc[:,2].values.tolist()
    city1_max_temp_values = city1_data.iloc[:,3].astype(float).values.tolist()
    city2_max_temp_values = city2_data.iloc[:,3].astype(float).values.tolist()
    context = {'date_range': week_dates, 
               'city1_data': city1_max_temp_values,
               'city2_data': city2_max_temp_values,
               'city1_name': city1,
               'city2_name': city2,
               }
    return context

def get_dates(days):
    current_date = datetime.now()

    days_prior = current_date - timedelta(days=days)

    current_date_str = current_date.strftime('%Y-%m-%d')
    days_prior_str = days_prior.strftime('%Y-%m-%d')

    return days_prior_str, current_date_str