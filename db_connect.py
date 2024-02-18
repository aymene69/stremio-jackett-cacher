import psycopg2
import os

def db_connect():
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    host = os.environ.get('DB_HOST')
    port = os.environ.get('DB_PORT')
    database = os.environ.get('DB_NAME')
    return psycopg2.connect(user = user,
                            password = password,
                            host = host,
                            port = port,
                            database = database)
                            
