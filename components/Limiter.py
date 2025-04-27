from datetime import datetime
class TokenBucketLimiter:
    """
    for simulation sake, units will be in ms
    """
    def __init__(self,bucket_size, refill_rate, server):
        self.bucket_size = bucket_size
        self.refill_rate = refill_rate
        self.server = server
        self.buckets = {} # this is via the IP address
        
    
    """
    takes in a request
    
    """
    def process_request(self,request):
        # check if the IP address is there, if not there, just create a bucket
        current_ip = request.ip_address
        if current_ip not in self.buckets:
            self.buckets[current_ip] = self.bucket_size
        
        # check current bucket
        if self.buckets[current_ip] <= 0:
            print(f"Bucket limit exceeded for {current_ip}!\n")
            return
        self.buckets[current_ip] -= 1
        self.server.process_request(request)
        print(f"Tokens left at {str(datetime.now().timestamp())} for address {current_ip} : {str(self.buckets[current_ip])}\n")
        
    def refill_buckets(self):
        """
        refills all buckets
        excess tokens will overflow thus they will not be counted
        """
        for ip_address in self.buckets:
            self.buckets[ip_address] = self.bucket_size
            print(f"{str(self.bucket_size)} tokens are refilled at {str(datetime.now().timestamp())}\n")