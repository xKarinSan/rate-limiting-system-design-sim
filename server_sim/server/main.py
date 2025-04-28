from fastapi import FastAPI
from fastapi.middleware import Middleware
from pydantic import BaseModel

from datetime import datetime
from uvicorn import run

app = FastAPI()

# rate_limiting_middleware = Middleware()


class Request(BaseModel):
    ip_address: str
    timestamp:float = datetime.now().timestamp()
    payload: str


app.get("/")
def hello_world():
    return {
        "message":"Hello world!"
    }

app.post("/send")
def send_request():
    
    return {
        "message":"Request processed!"
    }
    

if __name__ == "__main__":
    run("main:app",host="127.0.0.1", port=8000,reload=True)
    