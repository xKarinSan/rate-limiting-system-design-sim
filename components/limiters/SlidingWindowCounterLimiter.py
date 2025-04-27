from math import floor

class SlidingWindowCounterLimiter:
    def __init__(self,server,limit = 20):
        self.limit = limit
        self.store = {
            
        }
        self.server = server
        
    def process_request(self,request):
        
        """
        takes in request
        """
        curr_id = request.id
        curr_ip = request.ip_address
        curr_timestamp = request.timestamp
        rounded_timestamp = floor(curr_timestamp)
        previous_timestamp = rounded_timestamp - 1
        # check if window is there
        if curr_ip not in self.store:
            self.store[curr_ip] = {}
            
        # check for timestamp
        if rounded_timestamp not in self.store[curr_ip]:
            self.store[curr_ip][rounded_timestamp] = 0
            
        if previous_timestamp not in self.store[curr_ip]:
            self.store[curr_ip][previous_timestamp] = 0
        
        # calculate overlap:
        current_overlap = curr_timestamp - rounded_timestamp
        current_requests = (current_overlap *  self.store[curr_ip][rounded_timestamp]) + ((1-current_overlap) *  self.store[curr_ip][previous_timestamp])
        # if its there, check for limit
        if current_requests >= self.limit:
            print(f"Rate limit exceeded for {curr_ip}\n")
            return
        
        for timestamp in list(self.store[curr_ip].keys()):
            if timestamp < previous_timestamp:
                del self.store[curr_ip][timestamp]
                
        #if limit exceed, return 
        self.store[curr_ip][rounded_timestamp] += 1
        self.server.process_request(request)
    
        print(f"Processing request {curr_id} from {curr_ip}\n")