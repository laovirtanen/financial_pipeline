# AWS Lambda Financial Data Pipeline

This project is a fully automated financial data pipeline that fetches data from the FRED (Federal Reserve Economic Data) API and stores it in an Amazon S3 bucket. The system includes error monitoring using CloudWatch and automated dashboards using Amazon QuickSight.

 ## Project Architecture
 
**FRED API:** Fetches financial data (e.g., GDP) from the FRED API. <br/>
**AWS Lambda:** A serverless function that runs the pipeline to fetch and process data. <br/>
**Lambda Layer**: https://github.com/keithrozario/Klayers repo used for layer adaption.<br/>
**Amazon S3:** Stores the fetched financial data as CSV files. <br/>
**Amazon EventBridge:** Automates the pipeline execution by triggering the Lambda function on a schedule. <br/>
**CloudWatch:** Monitors the Lambda function and triggers alerts in case of failures. <br/>
**Amazon QuickSight:** Visualizes the data stored in S3 and automatically updates the dashboard with fresh data. <br/>



## Features

**Automated Fetching:** Data is fetched regularly via EventBridge automation. <br/>
**Serverless Architecture:** Utilizes AWS Lambda to process data without provisioning servers. <br/>
**Error Monitoring:** CloudWatch alarms notify on errors or failed executions. <br/>
**Data Storage:** Data is stored in S3 for long-term storage and easy access. <br >
**Dashboarding:** The data is visualized in Amazon QuickSight, automatically updated with the new data.
![Screenshot 2024-09-07 133200](https://github.com/user-attachments/assets/396a4238-bab6-4a6f-85f3-cd49c7bfcdc8)

## Getting Started
### Prerequisites
AWS account with access to Lambda, S3, EventBridge, CloudWatch, and QuickSight. <br />
FRED API key from the Federal Reserve.

## Setup
1. Clone the repository
2. `git clone https://github.com/laovirtanen/financial_pipeline.git`
3. Set up environment variables:

BUCKET_NAME: Name of the S3 bucket. <br/>
FRED_API_KEY: Your API key from the FRED service. <br/>
SERIES_ID: FRED data series ID (e.g., "GDP"). <br/>
Deploy the Lambda function via the AWS Console or AWS CLI.

### Automation
EventBridge is used to schedule the function to fetch data automatically at set intervals.
CloudWatch Alarms are configured to monitor failures in the function.

## Future Improvements
Integrating more FRED datasets.
Expanding the dashboard to cover additional financial metrics.
Adding notifications via SNS or other messaging services for critical alerts.
Adjust the dashboard for improved metrics and visuality.
![Screenshot 2024-09-07 131834](https://github.com/user-attachments/assets/d43073b5-3c24-4664-81ea-bf7856f060ed)
![Screenshot 2024-09-07 130923](https://github.com/user-attachments/assets/f6117181-4e4c-4121-9895-728b77c37d80)
