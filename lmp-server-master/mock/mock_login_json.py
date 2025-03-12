'''
@Project ：lmp-server-master 
@File    ：mock_login_json.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/11 15:57 
'''
menulist_admin_json = f"""
[
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
"""


menulist_user_json = f"""
[
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
"""