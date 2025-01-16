import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2f72e9a816b51eae65475c9faa253efd'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registration = {
    "name": "Бульбазавр",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "195699",
    "name": "Jonh",
    "photo_id": 2
}
body_pokeball = {
    "pokemon_id": "195699"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)

print(response.text)'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)

print(response.text)'''

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_pokeball)

print(response.text)