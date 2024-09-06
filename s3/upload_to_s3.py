import boto3

def upload_to_s3(local_file, bucket_name, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket_name, s3_file)
        print(f'File {local_file} uploaded to {bucket_name} as {s3_file}')
    except Exception as e:
        print(f'Failed to upload to s3: {e}')

