from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
# from fastapi.middleware import Middleware
from pydantic import BaseModel
from uvicorn import run
from cache import redis_cache

app = FastAPI()

RATE_LIMIT_PER_SEC = 20
@app.middleware("http")
async def rate_limiting_middleware(request:Request, call_next):
    if request.url.path != "/send":
        response = await call_next(request)
        return response
    else:
        fake_request = await request.json()
        ip_address = str(fake_request["ip_address"])
        current_count = 0
        print(f"redis_cache.get(ip_address):{redis_cache.get(ip_address)}")
        
        current_count = redis_cache.get(ip_address)

        if current_count is None:
            current_count = 0
        else:
            current_count = int(current_count) 
            
        if current_count >= RATE_LIMIT_PER_SEC:
            print("current_count:",current_count)
            return JSONResponse(
                status_code=429,
                content={"message": f"Rate limit {ip_address} exceeded"}
            )
        
        redis_cache.incr(ip_address) 
        redis_cache.pexpire(ip_address,1000)
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
    