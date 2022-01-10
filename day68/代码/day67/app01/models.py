from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=32,verbose_name='用户名')
    age = models.IntegerField(verbose_name='年龄')
    gender_choices = (
        (1,'male'),
        (2,'female'),
        (3,'others')
    )
    gender = models.IntegerField(choices=gender_choices,verbose_name='性别')


class Book(models.Model):
    title = models.CharField(max_length=32)