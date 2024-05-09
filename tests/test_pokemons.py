import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'c33d0ef54ba97d65f3daa821520e9068'
HEADER = {
        'Content-Type': 'application/json',
        "trainer_token": TOKEN
          }
TREINER_ID = '2298'


def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id' : TREINER_ID})
    assert response.status_code == 200
    
#Проверка, что ответ запрос GET /trainers приходит с кодом 200
def test_trainer_ctatus_code():
    response_status = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TREINER_ID})
    assert response_status.status_code == 200

#Проверка, что в ответе приходит строчка с именем твоего тренера        
def test_trainer_id():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TREINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Aleksandr'
    
@pytest.mark.parametrize('key, value',[('id',TREINER_ID),('trainer_name','Aleksandr'),('city','Moscow')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TREINER_ID})
    assert response_parametrize.json()['data'][0][key] == value