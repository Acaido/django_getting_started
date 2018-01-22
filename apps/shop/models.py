from django.db import models

from apps.shop.custom_checks import percentage


class Group(models.Model):
    name = models.CharField('название', max_length=50)

    class Meta:
        verbose_name = 'группа товаров'
        verbose_name_plural = 'группы товаров'


class Product(models.Model):
    name = models.CharField('наименование', max_length=100)
    # Для этого дела есть стрононние модули. Нам пока хватит флоата.
    price = models.FloatField('цена')
    available = models.BooleanField('есть в наличии', default=True)
    # Сомневаюсь насчет 1 ко многим. Возможно тут нужно многие ко многим.
    group = models.ForeignKey('Group', on_delete=models.CASCADE,
                              verbose_name='группа товаров')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Discount(models.Model):
    value = models.PositiveIntegerField('%', validators=[percentage])
    group = models.OneToOneField('Group', on_delete=models.CASCADE,
                                 verbose_name='группа товаров')

    class Meta:
        verbose_name = 'скидка'
        verbose_name_plural = 'скидки'
