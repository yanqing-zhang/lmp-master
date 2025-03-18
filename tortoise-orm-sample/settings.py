'''
@Project ：tortoise-orm-sample 
@File    ：settings.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/17 11:17 
'''
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TORTOISE_ORM: dict = {
            "connections": {
                # MySQL/InnoDB configuration
                # Install with: tortoise-orm[asyncmy]
                "mysql": {
                    "engine": "tortoise.backends.mysql",
                    "credentials": {
                        "host": "localhost",  # Database host address
                        "port": 3306,  # Database port
                        "user": "root",  # Database username
                        "password": "123456",  # Database password
                        "database": "students",  # Database name
                    },
                },

            },
            "apps": {
                "models": {
                    "models": ["app.models"],
                    "default_connection": "mysql",
                },
            },
            "use_tz": False,  # Whether to use timezone-aware datetimes
            "timezone": "Asia/Shanghai",  # Timezone setting
        }