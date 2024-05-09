import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'c33d0ef54ba97d65f3daa821520e9068'
HEADER = {
        'Content-Type': 'application/json',
        "trainer_token": 'c33d0ef54ba97d65f3daa821520e9068'
          }

POKEMON_ID = "17161"

BODY_NEW_POK = {
    "name": "Sigurd",
    "photo": "https://dolnikov.ru/pokemons/albums/955.png"
}
# создаем покемона
response =  requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_NEW_POK)
print(response.text)

POKEMON_ID1 = response.json()['id']

BODY_PUT_POK = {
    "pokemon_id": POKEMON_ID1,
    "name": "pikachy",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

BODY_ADD_POKEBALL = {
    "pokemon_id": POKEMON_ID1
}
# Изменить покемона
response_put_pok = requests.put(url = f'{URL}/pokemons',headers=HEADER, json=BODY_PUT_POK)
print(response_put_pok.json())

# Поймать покемона в покебол
response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER, json= BODY_ADD_POKEBALL)
print(response_add_pokeball.json())





