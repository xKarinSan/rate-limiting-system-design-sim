from datetime import datetime
class FakeQueue:
    def __init__(self,server,queue_size=50):
        self.queue = []
        self.queue_size = queue_size
        self.server = server

    """
    check if queue is empty
    """
    def queue_is_empty(self):
        return len(self.queue) == 0
    
    """
    check if queue is full
    """
    def queue_is_full(self):
        return len(self.queue) == self.queue_size 
    
    """
    add request to queue
    """
    def add_request_to_queue(self,request):
        if self.queue_is_full():
            return {
                "message":"Queue size capped",
                "code":429
            }
        self.queue.append(request)

        return {
            "message":"Currently processing",
            "code":200
        }
        
    """
    take out process from queue
    """
    def process_request(self):
        if self.queue_is_empty():
            return {
                "message":"Queue is empty"
            }
        curr_request = self.queue.pop(0)
        self.server.process_request(curr_request)
        return {
            "message":f"Request {curr_request.id} is sent for processing at {str(datetime.now().timestamp())}"
        }