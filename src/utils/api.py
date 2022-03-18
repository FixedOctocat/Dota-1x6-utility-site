import json
import requests

from http import HTTPStatus


API_URL = "http://old.dota1x6.com/api/"


def leaderboard():
    data = requests.get(API_URL + 'leaderboard')

    if data.status_code != HTTPStatus.OK:
        return None

    return json.loads(data.text)