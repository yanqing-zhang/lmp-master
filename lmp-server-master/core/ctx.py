'''
@Project ：lmp-server-master 
@File    ：ctx.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/12 15:24 
'''
import contextvars

from starlette.background import BackgroundTasks

CTX_USER_ID: contextvars.ContextVar[int] = contextvars.ContextVar("user_id", default=0)
CTX_BG_TASKS: contextvars.ContextVar[BackgroundTasks] = contextvars.ContextVar("bg_task", default=None)
