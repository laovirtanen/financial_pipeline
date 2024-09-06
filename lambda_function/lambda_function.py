import os
from pathlib import Path
from fetch_data.fetch_data import fetch_economic_data
from s3.upload_to_s3 import upload_to_s3
# from dotenv import load_dotenv


# Load environment variables
# Removed from labda

bucket_name = os.getenv('BUCKET_NAME')
fred_api_key = os.getenv('FRED_API_KEY')
series_id = os.getenv('SERIES_ID', 'GDP')



def lambda_handler(event, context):
    """
    This function serves as the entry point for AWS Lambda.
    It fetches economic data from FRED API and upload it to S3.
    """

    # Fetch data from FRED API using fetch_economic function
    data = fetch_economic_data(series_id, fred_api_key)

    # Check if running in Lambda or locally, and set data_dir accordingly
    if 'LAMBDA_TASK_ROOT' in os.environ:
        # Lambda environment
        data_dir = Path('/tmp/data')
    else:
        # Local environment (Windows/Linux/Mac)
        data_dir = Path('data')

    # Create the data directory if does not exist
    data_dir.mkdir(parents=True, exist_ok=True)


    # Save locally in the lambda's tmp directory
    local_file = data_dir / f'{series_id}.csv'
    data.to_csv(local_file)
    print(f'Data saved locally at {local_file}')

    # Upload the file to s3
    s3_file_key = f'data/{series_id}.csv'
    upload_to_s3(local_file.as_posix(), bucket_name, s3_file_key)
    print(f'Data uploaded successfully to s3://{bucket_name}/{s3_file_key}')


    return {
        'statusCode': 200,
        'body': f'Data uploaded successfully to {bucket_name}',
    }

if __name__ == "__main__":
    # Simulate the lambda event and context for local testing
    lambda_handler({}, {})