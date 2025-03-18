'''
@Project ：jwt-sample 
@File    ：token_sample_2.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/14 12:31 
'''
import uvicorn
from fastapi import FastAPI, Depends, HTTPException, Header, Request,status
from fastapi.security import APIKeyHeader

API_TOKEN = "dev"

app = FastAPI()

api_key_header = APIKeyHeader(name="Token")

async def api_token(token: str = Depends(APIKeyHeader(name="Token"))):
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized")
    return token

@app.get("/protected_route", dependencies=[Depends(api_token)])
async def protected_route():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)