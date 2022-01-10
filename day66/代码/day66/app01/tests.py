from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day66.settings")
    import django
    django.setup()

    from app01 import models
    # models.User.objects.create(username='jason',age=18,gender=1)
    # models.User.objects.create(username='egon',age=85,gender=2)
    # models.User.objects.create(username='tank',age=40,gender=3)
    # 存的时候 没有列举出来的数字也能存（范围还是按照字段类型决定）
    # models.User.objects.create(username='tony',age=45,gender=4)

    # 取
    # user_obj = models.User.objects.filter(pk=1).first()
    # print(user_obj.gender)
    # 只要是choices参数的字段 如果你想要获取对应信息 固定写法 get_字段名_display()
    # print(user_obj.get_gender_display())

    user_obj = models.User.objects.filter(pk=4).first()
    # 如果没有对应关系 那么字段是什么还是展示什么
    print(user_obj.get_gender_display())  # 4