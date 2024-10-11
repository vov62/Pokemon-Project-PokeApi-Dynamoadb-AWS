import boto3

# Specify the AWS region
region = 'us-west-2'

# Create a session using the default profile in ~/.aws/credentials
session = boto3.Session(profile_name='default', region_name=region)

# DynamoDB resource from the session
dynamodb = session.resource('dynamodb', region_name=region)

# Create DynamoDB table function
def create_dynamodb_table():
    table_name = 'pokemonsDBTable'

    try:
        # Check if the table exists first
        table = dynamodb.Table(table_name)
        table.load()  # This will trigger an exception if the table does not exist
        print(f"Table '{table_name}' already exists")
    except dynamodb.meta.client.exceptions.ResourceNotFoundException:
        try:
            # Create the DynamoDB table if it doesn't exist
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
                        'AttributeType': 'N'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
            # Wait until the table exists before continuing
            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
            print(f"Table '{table_name}' created successfully!")
        except Exception as e:
            print(f"Failed to create table: {str(e)}")
            return None
    return table

# Create EC2 instance function
def create_ec2_instance():
    try:
        # Get the EC2 service resource
        ec2_resource = session.resource('ec2')

        user_data_script = '''#!/bin/bash
        yum update -y
        yum install -y python3 python3-pip git

        # Clone the GitHub repository
        git clone https://github.com/vov62/Pokemon-Project-PokeApi-Dynamoadb-AWS /home/ec2-user/app

        # Navigate to the app directory
        cd /home/ec2-user/app

        # Install Python dependencies (if applicable)
        if [ -f requirements.txt ]; then
            pip3 install -r requirements.txt
        fi

        # Run the application in the background
        nohup python3 poke_task.py --draw yes &
        '''

        # Launch an EC2 instance
        instances = ec2_resource.create_instances(
            ImageId='ami-0d081196e3df05f4d',  
            InstanceType='t2.micro',
            KeyName='vockey',
            MinCount=1,
            MaxCount=1,
            UserData=user_data_script,
        )

        # Get the instance ID
        instance_id = instances[0].id
        print(f'Launched EC2 Instance ID: {instance_id}')

        # Wait until the instance is running
        instance = ec2_resource.Instance(instance_id)
        print('Waiting for instance to run...')
        instance.wait_until_running()

        # Reload the instance attributes to get the public IP address
        instance.load()
        print(f'EC2 instance is up and running!')

        return instance_id
    
    except Exception as e:
        print(f"An error occurred while creating the EC2 instance: {str(e)}")
        return None




def main():
    # create EC2 instance
    instance_id = create_ec2_instance()

    if instance_id:
        print(f"EC2 instance created successfully with ID: {instance_id}")

        # Create DynamoDB table
        dynamo_table = create_dynamodb_table()

        if dynamo_table:
            print(f"DynamoDB table created successfully!")
        else:
            print("Failed to create DynamoDB table.")
    else:
        print("Failed to create EC2 instance.")

# Run the main function
if __name__ == "__main__":
    main()
