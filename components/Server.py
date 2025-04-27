class FakeServer:
    def __init__(self):
        return
    
    def process_request(self,request):
        print(f"Request {request.id} from {request.ip_address} is being processed!\n")