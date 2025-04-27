import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.limiters.SlidingWindowLogLimiter import SlidingWindowLogLimiter
from components.general.RequestGenerator import FakeClient
from components.general.Server import FakeServer
from datetime import datetime

from random import randint
from time import sleep

if __name__ == "__main__":
    fake_server = FakeServer()
    leaking_bucket_limiter = SlidingWindowLogLimiter(fake_server)
    last_process_time = datetime.now().timestamp()
    
    
    client_count = 3
    clients = []
    
    for _ in range(client_count):
        new_client = FakeClient()
        clients.append(new_client)
        
    for i in range(1000):
        current_time = datetime.now().timestamp()
        sleep(randint(0,75)/1000)
        clients[randint(0, client_count-1)].generate_request(leaking_bucket_limiter)