import requests
import pytest

# URL и токен тренера
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '28bcdde7fd8d19b29a45e3a65871c68c'

# Заголовки запроса, включая токен
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN  # Передача токена в заголовке с именем 'trainer_token'
}

# id тренера
id_trainers = {"trainer_id" : 4614}

# Отправка GET запроса для получения информации о тренерах
def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers')
    assert response.status_code == 200

# Отправка GET запроса для получения информации о тренере
def test_part_of_response_trainer_id():
    response = requests.get(url = f'{URL}/v2/trainers', params = id_trainers)
    assert response.status_code == 200
    assert response.json()['data'][0]['trainer_name'] == 'Krotzim'

# Набор тестовых данных для параметризации теста
# Содержит пары ключ-значение, которые будут проверяться в теле ответа
CASES = [
    ('trainer_name', 'Krotzim'),
    ('city', 'Moscow')
]


@pytest.mark.parametrize('key, value', CASES)

 # Параметризованный тест для проверки значений в теле ответа и отправка GET запроса для получения информации о тренере
def test_parametrize_body(key, value):
    response = requests.get(url = f'{URL}/v2/trainers', params = id_trainers)
    assert response.status_code == 200
    assert response.json()['data'][0][key] == value