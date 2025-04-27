from datetime import datetime
from random import randint
from uuid import uuid4

class RequestBlock:
    def __init__(self,ip_address):
        self.timestamp = datetime.now().timestamp()
        self.ip_address = ip_address
        self.id = str(uuid4()).split("-")[0]

class FakeClient:
    def __init__(self):
        self.ip_address = ".".join(str(randint(0, 255)) for _ in range(4))
    
    """
    generates a request block
    """
    def generate_request(self,limiter):
        new_request = RequestBlock(self.ip_address)
        limiter.process_request(new_request)
    