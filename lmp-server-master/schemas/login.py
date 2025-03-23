'''
@Project ：lmp-server-master 
@File    ：login.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/20 12:25 
'''
from datetime import datetime

from pydantic import BaseModel, Field


class CredentialsSchema(BaseModel):
    username: str = Field(..., description="用户名称", example="admin")
    password: str = Field(..., description="密码", example="1")


class JWTOut(BaseModel):
    access_token: str
    username: str


class JWTPayload(BaseModel):
    user_id: int
    username: str
    is_superuser: bool
    exp: datetime
