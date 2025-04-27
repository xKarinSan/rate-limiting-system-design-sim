import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.limiters.FixedWindowCounterLimiter import FixedWindowLimiter
from components.general.RequestGenerator import FakeClient
from datetime import datetime

from random import randint
from time import sleep

if __name__ == "__main__":
    fixed_window_counter = FixedWindowLimiter(5)
    
    client_count = 3
    clients = []
    
    for _ in range(client_count):
        new_client = FakeClient()
        clients.append(new_client)
        
    for i in range(2000):
        sleep(randint(0,100)/1000)
        clients[randint(0, client_count-1)].generate_request(fixed_window_counter)
        
    