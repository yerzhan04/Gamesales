from data import data
import requests
import random
headers = {
    'accept': 'application/json',
}
while True:
    if random.randint(0, 100) == 8:
        json_data = random.choice(data)
        response = requests.post('http://127.0.0.1:8080/games/transaction', headers=headers, json=json_data)