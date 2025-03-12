'''
@Project ：lmp-server-master 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/10 10:58 
'''
from fastapi import APIRouter

from .user_api import router

users_router = APIRouter()
users_router.include_router(router, tags=["用户模块"])

__all__ = ["users_router"]
