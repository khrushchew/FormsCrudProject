from django.db import models


class Person(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=20)
    age = models.IntegerField(verbose_name='Возраст')
