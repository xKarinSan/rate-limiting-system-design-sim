class LeakngBucketLimiter:
    def __init__(self, queue):
        self.queue = queue
    
    def process_request(self,request):
        """ 
        takes in a request
        """
        # check if queue is full
        if self.queue.queue_is_full():
            print(f"Queue limit exceeded!\n")
            return
        # not full, add to queue
        print(f"Adding request {request.id} from {request.ip_address} to queue!\n")
        processing_status = self.queue.add_request_to_queue(request)
        print(processing_status["message"])
    