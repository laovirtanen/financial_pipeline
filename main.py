from fetch_data.fetch_data import fetch_economic_data
from s3.upload_to_s3 import upload_to_s3
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv('.env')

bucket_name = os.getenv('BUCKET_NAME')
fred_api_key = os.getenv('FRED_API_KEY')
series_id = os.getenv('SERIES_ID', 'GDP')

if __name__ == "__main__":
    series_id = series_id

    # Fetch data from FRED API
    data = fetch_economic_data(series_id, fred_api_key)

    data_dir = Path('data')

    data_dir.mkdir(exist_ok=True)

    local_file = data_dir / f'{series_id}.csv'

    # Make dir data if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save data locally
    data.to_csv(local_file, index=False)
    print(f"Data fetched and saved to {local_file}")

    # Download to s3
    bucket_name = bucket_name
    s3_file = f'data/{series_id}.csv'
    upload_to_s3(local_file.as_posix(), bucket_name, s3_file)
