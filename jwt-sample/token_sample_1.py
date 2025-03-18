'''
@Project ：jwt-sample 
@File    ：token_sample_1.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/14 11:52 
'''
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Header, Request,status
from fastapi.security import APIKeyHeader

API_TOKEN = "dev"

app = FastAPI()

api_key_header = APIKeyHeader(name="Token")

@app.get("/protected_route")
async def protected_route(token: str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized")
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)