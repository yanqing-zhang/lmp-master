'''
@Project ：jwt-sample 
@File    ：user_login.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/14 18:13 
'''
from typing import Annotated

from fastapi import Form, HTTPException

from auth import create_access_token
from password_sample_1 import verify_password


async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    user = await User.get(username=username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"user": username})
    return {"access_token": access_token, "token_type": "bearer"}