import time

from data_for_generator import data
import requests
import random
import time
headers = {
    'accept': 'application/json',
}

while True:
    time.sleep(1)
    n = random.randint(1, 10)
    for i in range(n):

        json_data = random.choice(data)
        response = requests.post('http://127.0.0.1:8080/games/transaction', headers=headers, json=json_data)
