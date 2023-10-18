from geopy.geocoders import Nominatim
import requests
import pandas as pd
from datetime import datetime, timedelta
import utils

def main():
    cities = ["Dammam","Jeddah","Al-Saih","Khaybar","Madinah","Mecca","Riyadh"]
    dataframe = pd.DataFrame()
    for city in cities:
        df = utils.fetch_data(city)
        dataframe = pd.concat([dataframe, df])
    
    dataframe.columns = ['lat','long','date','temp']
    dataframe.to_csv('../data/three_month_data.csv', index=False)

if __name__ == "__main__":
    main()
