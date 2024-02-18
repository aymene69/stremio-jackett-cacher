import base64
import psycopg2
from db_connect import db_connect
def get_result_movie(query):
    print("Getting movie results: " + query['title'] + " " + query['year'] + " " + query['language'])
    connection = db_connect()
    c = connection.cursor()
    # on est sur une base de données postgresql
    requete_sql = "SELECT * FROM movies WHERE LOWER(title) LIKE LOWER(REPLACE(%s, '.', ' ')) AND year = %s AND language = %s"
    c.execute(requete_sql, (f"%{query['title']}%", query['year'], query['language']))

    result = c.fetchall()
    connection.close()
    json_data = []
    for item in result:
        json_item = {"title": item[0], "trackers": item[1], "magnet": item[2], "files": item[3], "hash": item[4], "language": item[5], "quality": item[6], "qualitySpec": item[7], "seeders": item[8], "year": item[9], "size": item[10]}
        json_data.append(json_item)
    return json_data


def get_result_series(query):
    print("Getting series results: " + query['title'] + " " + query['season'] + query['episode'] + " " + query['language'])
    connection = db_connect()
    c = connection.cursor()
    requete_sql = "SELECT * FROM series WHERE LOWER(title) LIKE LOWER(REPLACE(%s, '.', ' ')) AND season = %s AND episode = %s AND language = %s AND isSeasonFile = 'false'"
    c.execute(requete_sql, (f"%{query['title']}%", query['season'], query['episode'], query['language']))
    results = c.fetchall()
    requete_sql = "SELECT * FROM series WHERE LOWER(title) LIKE LOWER(REPLACE(%s, '.', ' ')) AND season = %s AND language = %s AND isSeasonFile = 'true'"
    c.execute(requete_sql, (f"%{query['title']}%", query['season'], query['language']))
    results2 = c.fetchall()
    connection.close()
    json_data = []
    for item in results:
        json_item = {"title": item[0], "trackers": item[1], "magnet": item[2], "files": item[3], "hash": item[4], "language": item[5], "quality": item[6], "qualitySpec": item[7], "seeders": item[8], "size": item[9], "seasonfile": "false"}
        json_data.append(json_item)
    for item in results2:
        json_item = {"title": item[0], "trackers": item[1], "magnet": item[2], "files": item[3], "hash": item[4], "language": item[5], "quality": item[6], "qualitySpec": item[7], "seeders": item[8], "size": item[9], "seasonfile": "true"}
        json_data.append(json_item)
    return json_data
