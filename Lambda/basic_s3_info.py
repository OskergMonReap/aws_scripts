import json

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    region = event['Records'][0]['awsRegion']
    object = event['Records'][0]['s3']['object']['key']
    user   = event['Records'][0]['userIdentity']['principalId']
    
    print("Bucket: " + bucket)
    print("Region: " + region)
    print("User is " + user)
    
    return(object)
