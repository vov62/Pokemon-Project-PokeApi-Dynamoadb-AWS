import os
# from dotenv import load_dotenv
# import mysql.connector
import boto3

# Load environment variables from .env file
# load_dotenv()


# Use environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME', 'pokemons_db')
}


# def connect_to_database():
#     try:
#         conn = mysql.connector.connect(**DB_CONFIG)
#         return conn
    
#     except mysql.connector.Error as err:
#         print(f"Error: {err}")
#         return None
