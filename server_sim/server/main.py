from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
# from fastapi.middleware import Middleware
from pydantic import BaseModel
from datetime import datetime
from uvicorn import run
from cache import redis_cache
import json

app = FastAPI()

RATE_LIMIT_PER_SEC = 20
@app.middleware("http")
async def rate_limiting_middleware(request:Request, call_next):
    if request.url.path != "/send":
        response = await call_next(request)
        return response
    else:
        # rate limiting logic 
        fake_request = await request.json()
        
        # get the IP address too
        ip_address = str(fake_request["ip_address"])
        payload = fake_request["payload"]
        timestamp = datetime.now().timestamp()
        current_bucket = redis_cache.get(ip_address)
        
        if current_bucket:
            current_bucket = eval(current_bucket.decode('utf-8'))
        else:
            current_bucket = []
            
        earliest_timestamp = timestamp - 1
        while current_bucket and current_bucket[0][0] < earliest_timestamp:
            current_bucket.pop(0)
        if len(current_bucket) >= RATE_LIMIT_PER_SEC:
            return JSONResponse(
                status_code=429,
                content={"message": "Rate limit exceeded"}
            )
        
        current_bucket.append([timestamp,payload])
        redis_cache.set(ip_address, json.dumps(current_bucket))

        response = await call_next(request)
        return response

class FakeRequest(BaseModel):
    ip_address: str
    payload: str



@app.get("/")
def hello_world():
    return {
        "message":"Hello world!"
    }

@app.post("/send")
def send_request(request:FakeRequest):
    
    return {
        "message":"Request processed!"
    }
    

if __name__ == "__main__":
    run("main:app",host="127.0.0.1", port=8000,reload=True)
    