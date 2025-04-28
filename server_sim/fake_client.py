
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.general.RequestGenerator import generate_random_ip
from requests import post
from random import randint

def generate_clients(n):
    return [generate_random_ip() for i in range(n)]

def generate_requests(request_count,clients):
    client_count = len(clients)
    for i in range(request_count):
        current_client  = clients[randint(0,client_count-1)]
        mock_request = {
            "ip_address":current_client,
            "payload":"Testing payload"
        }
        res = post(
            "http://127.0.0.1:8000/send",
            json = mock_request
        )
        print(res.json())

if __name__ == "__main__":
    curr_clients = generate_clients(20)
    generate_requests(500,curr_clients)