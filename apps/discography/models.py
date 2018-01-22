from django.db import models


class Band(models.Model):
    name = models.CharField('группа', max_length=50)
    created = models.DateField('дата основания')
    broke_up = models.DateField('распалась', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'


class Performer(models.Model):
    first_name = models.CharField('имя', max_length=20)
    last_name = models.CharField('фимилия', max_length=20)
    band = models.ManyToManyField(
        'Band',
        through='PerformerBand',
        through_fields=('performer', 'band'),
        verbose_name='группа'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}'

    class Meta:
        verbose_name = 'исполнитель'
        verbose_name_plural = 'исполнители'


class PerformerBand(models.Model):
    performer = models.ForeignKey('Performer', on_delete=models.CASCADE)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)
    member = models.BooleanField()
    # Так сможем узнать (если когда-нибудь понадобится), в составе какой группы
    # находился артист, учавствуя в исполнении данной композиции.
    member_from = models.DateField()
    member_to = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.performer}/{self.band}/member({self.member})'

    class Meta:
        # В одно время можно состоять только в одной группе
        unique_together = ('performer', 'member')
        verbose_name = 'исполнитель -> группа'
        verbose_name_plural = 'исполнители / группы'


class Genre(models.Model):
    name = models.CharField('название', max_length=25)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'


class Album(models.Model):
    name = models.CharField('название', max_length=25)
    published = models.DateField('дата издания')

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'


class Track(models.Model):
    name = models.CharField('название', max_length=50)
    performer = models.ManyToManyField(
        'Performer', through='TrackPerformer', verbose_name='исполнитель')
    written = models.DateField('написан')
    genre = models.ForeignKey(
        'Genre', on_delete=models.PROTECT, verbose_name='жанр')
    # Один трек может повторяться в нескольких альбомах группы.
    # В тоже время каждый альбом содержит по несколько треков.
    album = models.ManyToManyField('Album', verbose_name='альбом')

    class Meta:
        verbose_name = 'трек'
        verbose_name_plural = 'треки'


class TrackPerformer(models.Model):
    track = models.ForeignKey('Track', on_delete=models.CASCADE)
    performer = models.ForeignKey('Performer', on_delete=models.CASCADE)
    band_role = models.ForeignKey('BandRole', on_delete=models.PROTECT)


class BandRole(models.Model):
    name = models.CharField('название', max_length=25)

    class Meta:
        verbose_name = 'роль в группе'
        verbose_name_plural = 'роли в группах'
