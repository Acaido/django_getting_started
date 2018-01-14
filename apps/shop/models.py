from django.db import models
from django.core.exceptions import ValidationError


class Group(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    # Для этого дела есть стрононние модули. Нам пока хватит флоата.
    price = models.FloatField()
    available = models.BooleanField(default=True)
    # Сомневаюсь насчет 1 ко многим. Возможно тут нужно многие ко многим.
    group = models.ForeignKey('Group', on_delete=models.CASCADE)


# Оставить здесь или запихать в какую-нибудь специальную директорию?
def percentage(value):
    if not 0 <= value <= 100:
        raise ValidationError(f'{value} must be in [0,100].')


class Discount(models.Model):
    value = models.PositiveIntegerField(validators=[percentage])
    group = models.OneToOneField('Group', on_delete=models.CASCADE)