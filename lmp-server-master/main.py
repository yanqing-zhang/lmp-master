'''
@Project ：lmp-server-master 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/10 10:52 
'''
import uvicorn
from fastapi import FastAPI
from utils.exceptions import SettingNotFound
from core.init_app import (
    init_data,
    make_middlewares,
    register_exceptions,
    register_routers,
)

try:
    from settings.config import settings
except ImportError:
    raise SettingNotFound("Can't import settings of config file")
def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_TITLE,
        description=settings.APP_DESCRIPTION,
        version=settings.VERSION,
        openapi_url="/openapi.json",
    )
    register_exceptions(app)
    register_routers(app, prefix="/api")
    return app


app = create_app()

if __name__== '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=9999, reload=True)