class SlidingWindowLogLimiter:
    def __init__(self,server, limit = 10):
        self.limit = limit
        self.store = {
            
        }
        self.server = server
    def process_request(self,request):
        curr_id = request.id
        curr_ip = request.ip_address
        curr_timestamp = request.timestamp
        rounded_timestamp = int(curr_timestamp)
        
        if curr_ip not in self.store:
            self.store[curr_ip] = []
        
        while self.store[curr_ip] and self.store[curr_ip][0] < rounded_timestamp - 1:
            self.store[curr_ip].pop(0)
            
        if len(self.store[curr_ip]) < self.limit:
            print(f"Processing request {curr_id} from {curr_ip}\n")
            self.store[curr_ip].append(curr_timestamp)
            self.server.process_request(request)
        else:
            print(f"Rate limit exceeded for {curr_ip}\n")