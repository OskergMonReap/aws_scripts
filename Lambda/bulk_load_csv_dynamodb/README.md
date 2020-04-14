# Bulk Load CSV Files into DynamoDB
#### Transform CSV files uploaded to S3 into Python dictionaries and load into DynamoDB

#### Pre-Reqs
- AWS Account
- User or Role with proper permissions for:
  - Cloudformation
  - DynamoDB
  - S3
  - Lambda
- Data in csv formatted file
  - *If using the quickstart or full solution, you must use `movies.csv` from this repo due to the DynamoDB Table schema*

#### Quickstart
Included a Cloudformation template that creates the required S3 bucket, DynamoDB table and IAM role for our Lambda Function. If treating this as a lab, where you must author your own function, trigger and bucket policy, deploy `csv_lab.yml`. This will only create the required bucket, table and role to use for our lambda. The `csv` file isn't particularly small, so helpful reminder to toy with the memory (which directly affects CPU) and timeout duration for your function.

#### Full Solution
For an all-in-one solution, deploy `csv_full.yml`. This will create our bucket, table, role and lambda function all in one, requiring a unique bucket name as a parameter at launch.
