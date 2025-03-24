'''
@Project ：tortoise-orm-samples 
@File    ：config.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/24 9:32 
'''
TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": "localhost",
                "port": "3306",
                "user": "root",
                "password": "123456",
                "database": "llm_app_db",
                "charset": "utf8mb4",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["models.permissions", "aerich.models"],  # 确保路径正确
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai",
}