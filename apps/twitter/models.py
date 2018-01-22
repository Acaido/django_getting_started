from django.db import models
from django.contrib import admin


class User(models.Model):
    first_name = models.CharField('имя', max_length=20)
    mid_name = models.CharField('второе имя', max_length=10,
                                blank=True, null=True)
    last_name = models.CharField('фамилия', max_length=20)
    nick_name = models.CharField('никнейм', max_length=30)
    mail = models.EmailField()

    def __str__(self):
        return (f'{self.first_name} '
                f'{(lambda x: x if x is not None else "")(self.mid_name)} '
                f'{self.last_name}')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Post(models.Model):
    author = models.ForeignKey('User', models.CASCADE, verbose_name='автор')
    published = models.DateTimeField('дата публикации', auto_now=True)
    updated = models.DateTimeField('дата обновления', blank=True, null=True)
    content = models.TextField('контент')
    likes = models.PositiveIntegerField('нравится', default=0)
    dislikes = models.PositiveIntegerField('не нравится', default=0)
    # Вместо того, чтобы удалять из базы, лишь только помечаем, как удаленные.
    # Большой брат на стреме :(
    removed = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Twit(Post):
    # Хотя в твиттере нет хидеров, только хэштеги. Потом можно удалить.
    header = models.TextField('заголовок', max_length=200)
    tag = models.ManyToManyField('Tag')

    def __str__(self):
        tags = ', '.join(str(tag) for tag in self.tag.all())
        return f'{self.header}/{self.author}/({tags})'

    class Meta:
        verbose_name = 'твит'
        verbose_name_plural = 'твиты'


class TwitAdmin(admin.ModelAdmin):
    fields = ('author', 'header', 'content', 'tag')


class Comment(Post):
    content = models.TextField('контент', max_length=128)
    reply_on = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        blank=True, null=True, verbose_name='ответ на')
    twit = models.ForeignKey('Twit', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}@{self.id}:{self.content}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Tag(models.Model):
    name = models.CharField('название', max_length=64, unique=True)

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
