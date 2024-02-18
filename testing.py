import requests
import json


LINK = "http://localhost:8001"

SERIES_PUSH_QUERY = [{'name': 'Legal Streaming Platform', 'title': 'Reacher Season 1 Original Version with French Subtitles (VOSTFR) HDTV', 'trackers': ['tracker:udp://tracker.fictitious1.org:1337/announce', 'tracker:udp://tracker.fictitious2.si:80/announce', 'tracker:udp://tracker.fictitious3.org:6969/announce', 'tracker:udp://tracker.fictitious4.com:6969/announce', 'tracker:udp://tracker.fictitious5.net:1337/announce', 'tracker:udp://tracker.fictitious6.lu:80/announce', 'tracker:udp://tracker.fictitious7.com:6969/announce', 'tracker:udp://tracker.fictitious8.com:6969/announce', 'tracker:udp://tracker.fictitious9.net:2740/announce', 'tracker:udp://tracker.fictitious10.com:2770/announce', 'tracker:http://tracker.fictitious11.info/announce', 'tracker:http://tracker.fictitious12.com/announce', 'tracker:udp://tracker.fictitious13.eu.org:451/announce', 'tracker:udp://tracker.fictitious14.us:6969/announce', 'tracker:http://tracker.fictitious15.com:2095/announce', 'tracker:udp://tracker.fictitious16.org:2710/announce'], 'magnet': 'magnet:?xt=urn:btih:8f4ce27b835b4d890cfadc480e1a931243791367&tr=udp://tracker.fictitious1.org:1337/announce&tr=udp://tracker.fictitious2.si:80/announce&tr=udp://tracker.fictitious3.org:6969/announce&tr=udp://tracker.fictitious4.com:6969/announce&tr=udp://tracker.fictitious5.net:1337/announce&tr=udp://tracker.fictitious6.lu:80/announce&tr=udp://tracker.fictitious7.com:6969/announce&tr=udp://tracker.fictitious8.com:6969/announce&tr=udp://tracker.fictitious9.net:2740/announce&tr=udp://tracker.fictitious10.com:2770/announce&tr=http://tracker.fictitious11.info/announce&tr=http://tracker.fictitious12.com/announce&tr=udp://tracker.fictitious13.eu.org:451/announce&tr=udp://tracker.fictitious14.us:6969/announce&tr=http://tracker.fictitious15.com:2095/announce&tr=udp://tracker.fictitious16.org:2710/announce', 'files': [], 'hash': '8f4ce27b835b4d890cfadc480e1a931243791367', 'indexer': 'Legal Streaming Platform', 'quality': 'Unknown', 'qualitySpec': 'Unknown', 'seeders': '76', 'size': '3221225472', 'language': 'fr', 'type': 'series', 'season': 'S01', 'episode': 'E01', 'availability': True, 'seasonfile': True}]
MOVIE_PUSH_QUERY = [{'name': 'Legal Streaming Platform', 'title': 'The Beekeeper 2024 FRENCH WEBRIP x264 ', 'trackers': ['tracker:udp://tracker.fictitious1.org:1337/announce', 'tracker:udp://tracker.fictitious2.si:80/announce', 'tracker:udp://tracker.fictitious3.org:6969/announce', 'tracker:udp://tracker.fictitious4.eu.org:451/announce', 'tracker:udp://www.fictitioustracker.eu.org:451/announce', 'tracker:udp://bt1.fictitious.org:6969/announce', 'tracker:udp://movies.fictitious.net:6969/announce'], 'magnet': 'magnet:?xt=urn:btih:GDPFU5PIMQB7E6F6IXXFPAQ5JCALD6OH&tr=udp://tracker.fictitious1.org:1337/announce&tr=udp://tracker.fictitious2.si:80/announce&tr=udp://tracker.fictitious3.org:6969/announce&tr=udp://tracker.fictitious4.eu.org:451/announce&tr=udp://www.fictitioustracker.eu.org:451/announce&tr=udp://bt1.fictitious.org:6969/announce&tr=udp://movies.fictitious.net:6969/announce', 'files': [], 'hash': 'GDPFU5PIMQB7E6F6IXXFPAQ5JCALD6OH', 'indexer': 'Legal Streaming Platform', 'quality': 'Unknown', 'qualitySpec': 'Unknown', 'seeders': '3626', 'size': '1024353920', 'language': 'fr', 'type': 'movie', 'season': None, 'episode': None, 'availability': True, 'year': '2024'}]
SERIES_GET_QUERY = {'title': 'Reacher', 'season': 'S01', 'episode': 'E03', 'type': 'series', 'language': 'fr'}
MOVIE_GET_QUERY = {'title': 'The Beekeeper', 'year': '2024', 'type': 'movie', 'language': 'fr'}


def push_series_cache(query):
    print("Pushing series to cache")
    url = LINK + "/pushResult/series"
    response = requests.post(url, data=json.dumps(query))
    return response.json()

def push_movie_cache(query):
    print("Pushing movie to cache")
    url = LINK + "/pushResult/movie"
    response = requests.post(url, data=json.dumps(query))
    response.json()

def get_series_cache(query):
    print("Getting series from cache")
    url = LINK + "/getResult/series/"
    response = requests.get(url, json=query)
    return str(len(response.json())) + " results"

def get_movie_cache(query):
    print("Getting movie from cache")
    url = LINK + "/getResult/movie/"
    response = requests.get(url, json=query)
    return str(len(response.json())) + " results"

def main():
    if push_series_cache(SERIES_PUSH_QUERY) == None or "Success":
        print("Series pushed to cache")
    if push_movie_cache(MOVIE_PUSH_QUERY) == None or "Success":
        print("Movie pushed to cache")
    print(get_series_cache(SERIES_GET_QUERY))
    print(get_movie_cache(MOVIE_GET_QUERY))

main()