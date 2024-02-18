import psycopg2
from dotenv import dotenv_values
config = dotenv_values(".env")

def db_connect():
    user = config['DB_USER']
    password = config['DB_PASSWORD']
    host = config['DB_HOST']
    port = config['DB_PORT']
    database = config['DB_NAME']
    return psycopg2.connect(user = user,
                            password = password,
                            host = host,
                            port = port,
                            database = database)
                            