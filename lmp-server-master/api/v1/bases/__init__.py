'''
@Project ：lmp-server-master 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/19 16:19 
'''
from fastapi import APIRouter

from .login_api import router

bases_router = APIRouter()
bases_router.include_router(router, tags=["基础模块"])

__all__ = ["bases_router"]
