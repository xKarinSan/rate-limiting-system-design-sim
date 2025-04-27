import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.limiters.SlidingWindowCounterLimiter import SlidingWindowCounterLimiter
from components.general.RequestGenerator import FakeClient
from components.general.Server import FakeServer
from datetime import datetime

from random import randint
from time import sleep

if __name__ == "__main__":
    fake_server = FakeServer()
    sliding_window_counter = SlidingWindowCounterLimiter(fake_server,20)
    
    client_count = 3
    clients = []
    
    for _ in range(client_count):
        new_client = FakeClient()
        clients.append(new_client)
        
    for i in range(2000):
        sleep(randint(0,10)/1000)
        clients[randint(0, client_count-1)].generate_request(sliding_window_counter)
        
    