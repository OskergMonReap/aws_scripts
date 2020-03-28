import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName = 'Movies',
    KeySchema = [
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'    # Partition Key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'   # Sort Key
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print('Table Status: ', table.table_status)

print('Waiting for ', table.name, ' to complete creating...')
table.meta.client.get_waiter('table_exists').wait(TableName='Movies')
print('Table status: ', dynamodb.Table('Movies').table_status)
