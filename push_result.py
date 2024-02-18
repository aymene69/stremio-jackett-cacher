import base64
import sqlite3
import json
import psycopg2
from db_connect import db_connect


def push_result_movie(data):
    print("New entry: ", data)
    connection = db_connect()

    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS movies (title text, trackers text, magnet text, files text, hash text, language text, quality text, qualitySpec text, seeders text, year text, size text)")

    for elem in data:
        c.execute("SELECT * FROM movies WHERE hash = %s", (elem['hash'],))

        existing_entry = c.fetchone()
        if existing_entry is None:
            c.execute("INSERT INTO movies VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                      (elem['title'], json.dumps(elem['trackers']), elem['magnet'], json.dumps(elem['files']), elem['hash'], elem['language'], elem['quality'],
                       elem['qualitySpec'], elem['seeders'], elem['year'], elem['size']))
    connection.commit()
    connection.close()

def push_result_series(data):
    print("New entry: ", data)
    connection = db_connect()

    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS series (title text, trackers text, magnet text, files text, hash text, language text, quality text, qualitySpec text, seeders text, size text, season text, episode text, isSeasonFile text)")

    for elem in data:
        c.execute("SELECT * FROM series WHERE hash = %s", (elem['hash'],))

        existing_entry = c.fetchone()
        query = f"INSERT INTO series VALUES ('{elem['title']}', '{json.dumps(elem['trackers'])}', '{elem['magnet']}', '{json.dumps(elem['files'])}', '{elem['hash']}', '{elem['language']}', '{elem['quality']}', '{elem['qualitySpec']}', '{elem['seeders']}', '{elem['size']}', '{elem['season']}', '{elem['episode']}', '{elem['seasonfile']}')"
        if existing_entry is None:
            c.execute("INSERT INTO series VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                      (elem['title'], json.dumps(elem['trackers']), elem['magnet'], json.dumps(elem['files']), elem['hash'], elem['language'], elem['quality'],
                       elem['qualitySpec'], elem['seeders'], elem['size'], elem['season'], elem['episode'], elem['seasonfile']))
    connection.commit()
    connection.close()
