
from table_operations import create_dynamodb_table


def insert_item_to_dynamodb():
    
    table = create_dynamodb_table()

    if table is None:
        print("Failed to retrieve or create the table.")
        return
    
    try:
        table.put_item(
            Item={
                "id": 82,
                "name": "magneton",
                "height": 10,
                "weight": 600,
                "types": [
                    "electric",
                    "steel"
                ]
            }
        )
        print('item added successfully!')
    except Exception as e:
        print(f"failed to create item: {str(e)}")


# create_dynamodb_table_items()