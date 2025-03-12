'''
@Project ：lmp-server-master 
@File    ：enums.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/12 11:49 
'''
from enum import Enum, StrEnum


class EnumBase(Enum):
    @classmethod
    def get_member_values(cls):
        return [item.value for item in cls._member_map_.values()]

    @classmethod
    def get_member_names(cls):
        return [name for name in cls._member_names_]


class MethodType(StrEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"


class MenuType(StrEnum):
    CATALOG = "catalog"  # 目录
    MENU = "menu"  # 菜单