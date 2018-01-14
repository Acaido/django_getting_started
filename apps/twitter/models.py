from django.db import models
from django.contrib import admin


class User(models.Model):
    first_name = models.CharField(max_length=20)
    mid_name = models.CharField(max_length=10, blank=True, null=True)
    last_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=30)
    mail = models.EmailField()

    def __str__(self):
        return (f'{self.first_name} '
                f'{(lambda x: x if x is not None else "")(self.mid_name)} '
                f'{self.last_name}')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Post(models.Model):
    author = models.ForeignKey('User', models.CASCADE)
    published = models.DateTimeField(auto_now=True)
    # todo: нужно скрыть поля в админке и назначить функцию, которая будет изменять значение
    # Поля: updated, likes, dislikes, removed
    updated = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    # Вместо того, чтобы удалять из базы, лишь только помечаем, как удаленные.
    # Большой брат на стреме :(
    removed = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Twit(Post):
    # Хотя в твиттере нет хидеров, только хэштеги. Потом можно удалить.
    header = models.TextField(max_length=200)
    tag = models.ManyToManyField('Tag')

    def __str__(self):
        tags = ', '.join(str(tag) for tag in self.tag.all())
        return f'{self.header}/{self.author}/({tags})'


class TwitAdmin(admin.ModelAdmin):
    fields = ('author', 'header', 'content', 'tag')


class Comment(Post):
    content = models.TextField(max_length=128)
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True)
    twit = models.ForeignKey('Twit', on_delete=models.CASCADE)
    # Можно ли переопределить поле базового класса

    def __str__(self):
        return f'{self.author}@{self.id}:{self.content}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'#{self.name}'
