'''
@Project ：lmp-server-master 
@File    ：init_app.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/11 16:44 
'''
import shutil

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from tortoise.expressions import Q

from api import api_router
from core.middlewares import BackGroundTaskMiddleware, HttpAuditLogMiddleware
from utils.exceptions import (
    DoesNotExist,
    DoesNotExistHandle,
    HTTPException,
    HttpExcHandle,
    IntegrityError,
    IntegrityHandle,
    RequestValidationError,
    RequestValidationHandle,
    ResponseValidationError,
    ResponseValidationHandle,
)
from models.permission import Api, Menu, Role
from settings.enums import MenuType
from settings.config import settings

def make_middlewares():
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],  # 允许所有源，生产环境应指定具体源
            allow_credentials=True,
            allow_methods=["*"],  # 允许所有方法（包括OPTIONS）
            allow_headers=["*"],  # 允许所有头部
        ),
        # Middleware(
        #     HttpAuditLogMiddleware,
        #     methods=["GET", "POST", "PUT", "DELETE"],
        #     exclude_paths=[
        #         "/docs",
        #         "/openapi.json",
        #     ],
        # ),
    ]
    return middleware


def register_exceptions(app: FastAPI):
    app.add_exception_handler(DoesNotExist, DoesNotExistHandle)
    app.add_exception_handler(HTTPException, HttpExcHandle)
    app.add_exception_handler(IntegrityError, IntegrityHandle)
    app.add_exception_handler(RequestValidationError, RequestValidationHandle)
    app.add_exception_handler(ResponseValidationError, ResponseValidationHandle)


def register_routers(app: FastAPI, prefix: str = "/api"):
    app.include_router(api_router, prefix=prefix)


async def init_superuser():
    pass


async def init_menus():
    pass


async def init_apis():
    pass


async def init_db():
    pass


async def init_roles():
    pass

async def init_data():
    await init_db()
    await init_superuser()
    await init_menus()
    await init_apis()
    await init_roles()
