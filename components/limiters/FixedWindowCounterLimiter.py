class FixedWindowLimiter:
    def __init__(self,limit = 20):
        self.limit = limit
        self.store = {
            
        }
    
    def process_request(self,request):
        
        """
        takes in request
        """
        curr_id = request.id
        curr_ip = request.ip_address
        curr_timestamp = request.timestamp
        rounded_timestamp = int(curr_timestamp)
        # check if window is there
        if curr_ip not in self.store:
            self.store[curr_ip] = {}
            
        # check for timestamp
        if rounded_timestamp not in self.store[curr_ip]:
            self.store[curr_ip][rounded_timestamp] = 0
        
        # if its there, check for limit
        if self.store[curr_ip][rounded_timestamp] == self.limit:
            print(f"Rate limit exceeded for {curr_ip}\n")
            return
        
        #if limit exceed, return 
        self.store[curr_ip][rounded_timestamp] += 1
        print(f"Processing request {curr_id} from {curr_ip}\n")