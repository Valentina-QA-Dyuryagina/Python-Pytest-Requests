import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'вставить токен'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Вупсень",
    "photo": "https://dolnikov.ru/pokemons/albums/1007.png"
}
body_change = {
    "pokemon_id": "27166",
    "name": "Пупсень",
    "photo": "https://dolnikov.ru/pokemons/albums/1008.png"
}

body_catch = {
    "pokemon_id": "27166"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
