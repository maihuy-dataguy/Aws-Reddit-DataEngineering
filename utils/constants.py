import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET = parser.get(section='api_keys', option='reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

DATABASE_HOST = parser.get('database_airflow', ' database_host')
DATABASE_NAME = parser.get('database_airflow', ' database_name')
DATABASE_PORT = parser.get('database_airflow', ' database_port')
DATABASE_USERNAME = parser.get('database_airflow', ' database_username')
DATABASE_PASSWORD = parser.get('database_airflow', ' database_password')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')
