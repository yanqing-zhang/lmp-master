'''
@Project ：tortoise-orm-sample 
@File    ：simple_example_1.py
@IDE     ：PyCharm 
@Author  ：yanqing.zhang@
@Date    ：2025/3/17 10:08 
'''
from tortoise import fields, run_async
from tortoise.contrib.test import init_memory_sqlite
from tortoise.models import Model
from tortoise import Tortoise
from models.student_base_info import Student
from settings import Settings

class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    datetime = fields.DatetimeField(null=True)

    class Meta:
        table = "event"

    def __str__(self):
        return self.name
@init_memory_sqlite
async def run_1() -> None:
    event = await Event.create(name="Test")
    await Event.filter(id=event.id).update(name="Updated name")
    print(await Event.filter(name="Updated name").first())

    await Event(name="Test 2").save()
    print(await Event.all().values_list("id", flat=True))

    print(await Event.all().values("id", "name"))

async def run_2():
    await Tortoise.init(db_url="mysql://root:123456@localhost/students", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    stu = await Student.create(stu_name="x", stu_no="1002", stu_gender=1, stu_birthday="2025-03-17", yn=1)
    await Student.filter(id=stu.id).update(stu_name="z")

    print(await Student.filter(stu_name="z").first())

    # await Student(stu_name="Test 2").save()
    print(await Student.all().values_list("id", flat=True))
    print(await Student.all().values("id", "stu_name"))

async def run_3():
    await Tortoise.init(Settings.TORTOISE_ORM)
    await Tortoise.generate_schemas()

    stu = await Student.create(stu_name="t", stu_no="1002", stu_gender=1, stu_birthday="2025-03-17", yn=1)
    await Student.filter(id=stu.id).update(stu_name="t")

    print(await Student.filter(stu_name="h").first())

    # await Student(stu_name="Test 2").save()
    print(await Student.all().values_list("id", flat=True))
    print(await Student.all().values("id", "stu_name"))

if __name__ == "__main__":
    run_async(run_3())
