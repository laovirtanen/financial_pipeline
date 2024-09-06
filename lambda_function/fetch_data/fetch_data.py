import os
# from dotenv import load_dotenv
import requests
import pandas as pd

# Removed load dotenv from lambda
# load_dotenv('../../.env')

# Fetch API KEY from environment variables
FRED_API_KEY = os.getenv('FRED_API_KEY')

def fetch_economic_data(series_id, api_key):
    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={api_key}&file_type=json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['observations']
        df = pd.DataFrame(data)
        return df
    else:
        raise Exception(f'Data fetching failed with status code {response.status_code}')



