from django.db import models
from datetime import date


class Author(models.Model):
    first_name = models.CharField('имя', max_length=20)
    last_name = models.CharField('фамилия', max_length=20)
    birth_date = models.DateField('дата рождения')
    death_date = models.DateField('дата смерти', blank=True, null=True)

    @property
    def age(self):
        now = date.today() if self.death_date is None else self.death_date
        return (now - self.birth_date).days // 365

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}.'

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


# В идеале нужно разбить на типы (художественная, фантастика, документалка),
# затем на группы внутри. Например группа "Эпос" (проза) типа
# "художественная литература" включает в себя:
# роман-эпопея, роман, повесть, рассказ, новелла, притча, сказка. Получается,
# что каждое произведение имеет один жанр.
# Но в источниках зачастую смешивают понятия. Так, например, жанры "фантастика"
# и "киберпанк" (который не имеет группы как таковой). В общем, нужно
# как следует изучить вопрос.
# Пока не заморачиваемся и делаем просто "Жанр" - один на всех, и, вместо
# один ко многим, делаем многие ко многим.
class Genre(models.Model):
    name = models.CharField('название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class Book(models.Model):
    name = models.CharField('название', max_length=100, unique=True)
    published = models.IntegerField('дата публикации')
    genre = models.ManyToManyField(
        'Genre', verbose_name='жанр', related_name='book')
    author = models.ManyToManyField(
        'Author', verbose_name='автор', related_name='book')

    def __str__(self):
        authors = ', '.join(str(author) for author in self.author.all())
        genres = ', '.join(str(genre) for genre in self.genre.all())
        return f'{self.name}/{self.published}/{authors}/{genres}'

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
