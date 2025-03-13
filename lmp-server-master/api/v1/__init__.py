'''
@Project ：lmp-server-master 
@File    ：__init__.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/11 16:47 
'''
from fastapi import APIRouter

from core.dependence import DependPermisson


from .roles import roles_router
from .users import users_router

v1_router = APIRouter()


v1_router.include_router(users_router, prefix="/user", dependencies=[DependPermisson])
v1_router.include_router(roles_router, prefix="/role", dependencies=[DependPermisson])
