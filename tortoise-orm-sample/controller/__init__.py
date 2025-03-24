'''
@Project ：tortoise-orm-samples 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 11:25 
'''
'''
@Project ：tortoise-orm-samples 
@File    ：__init__.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 11:21 
'''
from .user_controller import router
from contextlib import asynccontextmanager
from fastapi import FastAPI,APIRouter
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from settings.config import TORTOISE_ORM

app = FastAPI()
app.include_router(router, prefix="/api")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 初始化 Tortoise-ORM
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()  # 生成数据库表
    # await init_data()  # 初始化数据
    yield
    await Tortoise.close_connections()  # 关闭数据库连接

# 注册 Tortoise-ORM

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,  # 已经在 lifespan 中生成
    add_exception_handlers=True,
)