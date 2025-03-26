'''
@Project ：tortoise-orm-samples 
@File    ：init_app.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 13:52 
'''
from contextlib import asynccontextmanager
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from settings.config import setting
from controller.user_controller import router

def register_routers(app: FastAPI, prefix: str = "/api"):
    app.include_router(router, prefix=prefix)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 初始化 Tortoise-ORM
    await Tortoise.init(config=setting.TORTOISE_ORM)
    await Tortoise.generate_schemas()  # 生成数据库表
    # await init_data()  # 初始化数据
    yield
    await Tortoise.close_connections()  # 关闭数据库连接

# 注册 Tortoise-ORM

def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Tortoise-ORM",
        description="FastAPI Tortoise-ORM",
        version="v1.0",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )
    register_routers(app, prefix="/api")
    return app


app = create_app()

register_tortoise(
    app,
    config=setting.TORTOISE_ORM,
    generate_schemas=False,  # 已经在 lifespan 中生成
    add_exception_handlers=True,
)