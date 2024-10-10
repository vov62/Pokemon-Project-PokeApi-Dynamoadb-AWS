import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-west-2')


def create_dynamodb_table():

    # dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table_name = 'pokemonsDBTable'

    try:
        # Check if the table exists first
        table = dynamodb.Table(table_name)
        table.load()  # This will trigger an exception if the table does not exist
        print(f"Table '{table_name}' already exists")

    except dynamodb.meta.client.exceptions.ResourceNotFoundException:

        try:
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'  # Partition key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'N'  # Using Number for id
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
            print(f"Table '{table_name}' created successfully!")
        except Exception as e:
            print(f"failed to create table: {str(e)}")
            return None
    
    return table


# create_dynamodb_table()



