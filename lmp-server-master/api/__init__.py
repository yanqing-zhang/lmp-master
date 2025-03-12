'''
@Project ：lmp-server-master 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/10 10:58 
'''
from fastapi import APIRouter

from .v1 import v1_router

api_router = APIRouter()
api_router.include_router(v1_router, prefix="/v1")


__all__ = ["api_router"]