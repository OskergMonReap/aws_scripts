# Bulk Load CSV Files into DynamoDB
#### Transform CSV files uploaded to S3 into Python dictionaries and load into DynamoDB

#### Pre-Reqs
Included a Cloudformation template that creates the required S3 bucket, DynamoDB table and IAM role for our Lambda Function. If treating this as a lab, where you must author your own function, deploy `csv_lab.yml`. This will only create the required bucket, table and role to use for our lambda. For an all-in-one solution, deploy `csv_full.yml`. This will create our bucket, table, role and lambda function.

For sample data to test, we will use the included `movies.csv` file.
