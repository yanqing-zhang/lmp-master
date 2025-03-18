'''
@Project ：tortoise-orm-sample 
@File    ：init_app.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/17 13:53 
'''
from aerich import Command
from settings import Settings


async def init_db():
    command = Command(tortoise_config=Settings.TORTOISE_ORM)
    try:
        await command.init_db(safe=True)
    except FileExistsError:
        pass

    await command.init()
    try:
        await command.migrate()
    except AttributeError:
        print("unable to retrieve model history from database, model history will be created from scratch")
        # shutil.rmtree("migrations")
        await command.init_db(safe=True)

    await command.upgrade(run_in_transaction=True)
