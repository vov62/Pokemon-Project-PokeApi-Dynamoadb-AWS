
from table_operations import create_dynamodb_table
from datetime import datetime
from boto3.dynamodb.conditions import Key, Attr


def insert_item_to_dynamodb():
    
    table = create_dynamodb_table()

    if table is None:
        print("Failed to retrieve or create the table.")
        return
    
    try:
        response = table.put_item(
            Item={
                "id": 194,
                "name": "wooper",
                "height": 4,
                "weight": 85,
                "types": [
                    "water",
                    "ground"
                ],
                "created_date": datetime.now().isoformat()
            }
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print('item added successfully!')
    except Exception as e:
        print(f"failed to create item: {str(e)}")


# create_dynamodb_table_items()
