import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'dsafsjajfjr342jr324j'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '18518'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_json():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID,})
    assert response_get.json()["data"][0]['trainer_name'] == 'yeves'
