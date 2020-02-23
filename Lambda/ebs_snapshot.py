import json
import boto3

# Setting ec2 client.
ec2 = boto3.client('ec2')

# Our lambda handler function!
def lambda_handler(event, context):
    # Printing event received.
    # print("Received event: " + json.dumps(event, indent=2))

    # print the rule arn to the logs so we can differentiate from others
    rule_name = event['resources']
    print(rule_name)

    # Setting the variable to loop through later.
    # Filtering by only looking for 'in-use' EBS volumes.
    total_ebs = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['in-use']}])

    # Looping through all in-use EBS volumes
    for volume in total_ebs['Volumes']:
    	# Creating the snaphsot for all volumes within our region.
        ec2.create_snapshot(VolumeId=volume['VolumeId'],Description=volume['Attachments'][0]['InstanceId'])

        print("All done with volume: " + volume['VolumeId'])
