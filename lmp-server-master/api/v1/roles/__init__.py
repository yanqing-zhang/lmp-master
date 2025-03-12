'''
@Project ：lmp-server-master 
@File    ：__init__.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/12 11:39 
'''
from fastapi import APIRouter

from .role_api import router

roles_router = APIRouter()
roles_router.include_router(router, tags=["角色模块"])

__all__ = ["roles_router"]
