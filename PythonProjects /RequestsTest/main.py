import requests

# URL и токен тренера
URL = 'https://api.pokemonbattle.ru'
TOKEN = '28bcdde7fd8d19b29a45e3a65871c68c'

# Заголовки запроса, включая токен
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN  # Передача токена в заголовке с именем 'trainer_token'
}

# id тренера
id_trainers = 4614

# Тело запроса для создания покемона
body_create_pok = {
    "name": "Бульбазавр",
    "photo_id": 1
}

# Отправка POST запроса для создания покемона
response_pok_post = requests.post(url = f'{URL}/v2/pokemons', headers = HEADERS, json = body_create_pok)
print(response_pok_post.text)

# Извлечение pokemon_id из ответа
response_data = response_pok_post.json()
pokemon_id = response_data.get("id")

# Тело запроса для обновления покемона с полученным pokemon_id
body_change_pok = {
    "pokemon_id": pokemon_id,
     "name": "New Name",
    "photo_id": 2
}

# Отправка PUT запроса для обновления покемона
response_pok_put = requests.put(url = f'{URL}/v2/pokemons', headers = HEADERS, json = body_change_pok)

# Вывод ответа на PUT запрос
print(response_pok_put.text)

# Тело запроса что бы поймать покемона в покебол с полученным pokemon_id
body_add_pokeball_pok = {
    "pokemon_id": pokemon_id
}

# Отправка POST запроса что бы поймать покемона в покебол
response_add_pokeball_pok_post = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADERS, json = body_add_pokeball_pok)

# Вывод ответа на POST запрос
print(response_add_pokeball_pok_post.text)