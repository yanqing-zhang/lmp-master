'''
@Project ：lmp-server-master 
@File    ：mock_login_json.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/11 15:57 
'''
import pandas as pd
import datetime
from dateutil import tz
from models.permission import LoginUser

menulist_admin_st = [
    {
        "name": "数据看板",
        "url": "/dashboard",
        "icon": "DataLine"
    },
    {
        "name": "财务应用",
        "url": "/financial",
        "icon": "Lightning",
        "children": [
            {
                "name": "分析管理列表",
                "url": "/financial/analysislist",
                "icon": "VideoCamera"
            },
            {
                "name": "智能分析设置",
                "url": "/financial/analysis",
                "icon": "DataAnalysis"
            }
        ]
    },
    {
        "name": "权限设置",
        "url": "/permission",
        "icon": "Setting",
        "children": [
            {
                "name": "人员管理",
                "url": "/permission/userlist",
                "icon": "VideoCamera"
            },
            {
                "name": "公司管理",
                "url": "/permission/companylist",
                "icon": "DataAnalysis"
            },
            {
                "name": "部门管理",
                "url": "/permission/departmentlist",
                "icon": "DataAnalysis"
            },
            {
                "name": "角色管理",
                "url": "/permission/rolelist",
                "icon": "DataAnalysis"
            },
            {
                "name": "资源管理",
                "url": "/permission/resourcelist",
                "icon": "DataAnalysis"
            }
        ]
    },
    {
        "name": "个人中心",
        "url": "/profile",
        "icon": "User"
    }
]

menulist_admin_json = pd.json_normalize(menulist_admin_st).to_json(orient='records')

menulist_user_str = [
    {
        "name": "数据看板",
        "url": "/dashboard",
        "icon": "DataLine"
    },
    {
        "name": "财务应用",
        "url": "/financial",
        "icon": "Lightning",
        "children": [
            {
                "name": "分析管理列表",
                "url": "/financial/analysislist",
                "icon": "VideoCamera"
            },
            {
                "name": "智能分析设置",
                "url": "/financial/analysis",
                "icon": "DataAnalysis"
            }
        ]
    },
    {
        "name": "个人中心",
        "url": "/profile",
        "icon": "User"
    }
]

mock_user_list = []
def create_user():
    login_user = LoginUser()
    login_user.user_id = "1001"
    login_user.login_name = "admin"
    login_user.login_pwd = "1"
    login_user.latest_login_time = datetime.datetime.now(tz=tz.tzlocal())  # "2025-03-11 15:57:00"
    if login_user not in mock_user_list:
        mock_user_list.append(login_user)
    return login_user

menulist_user_json = pd.json_normalize(menulist_user_str).to_json(orient='records')