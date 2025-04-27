import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.Limiter import TokenBucketLimiter
from components.RequestGenerator import FakeClient
from components.Server import FakeServer
from datetime import datetime

from random import randint
from time import sleep


if __name__ == "__main__":
    fake_server = FakeServer()
    token_bucket_limiter = TokenBucketLimiter(10,5000,fake_server)
    last_refill_time = datetime.now().timestamp()
    
    client_count = 3
    clients = []
    
    for _ in range(client_count):
        new_client = FakeClient()
        clients.append(new_client)
        
    for i in range(1000):
        current_time = datetime.now().timestamp()
        if current_time > last_refill_time + 5:
            token_bucket_limiter.refill_buckets()
            last_refill_time = current_time
            
        sleep(randint(0,500)/1000)
        clients[randint(0, client_count-1)].generate_request(token_bucket_limiter)
        
    