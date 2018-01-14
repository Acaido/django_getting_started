from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateField()
    broke_up = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Performer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    band = models.ManyToManyField(
        'Band',
        through='PerformerBand',
        through_fields=('performer', 'band')
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name[0]}'


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


class Genre(models.Model):
    name = models.CharField(max_length=25)


class Album(models.Model):
    name = models.CharField(max_length=25)
    published = models.DateField()


class Track(models.Model):
    name = models.CharField(max_length=50)
    performer = models.ManyToManyField('Performer', through='TrackPerformer')
    written = models.DateField()
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    # Один трек может повторяться в нескольких альбомах группы.
    # В тоже время каждый альбом содержит по несколько треков.
    album = models.ManyToManyField('Album')


class TrackPerformer(models.Model):
    track = models.ForeignKey('Track', on_delete=models.CASCADE)
    performer = models.ForeignKey('Performer', on_delete=models.CASCADE)
    band_role = models.ForeignKey('BandRole', on_delete=models.PROTECT)


class BandRole(models.Model):
    name = models.CharField(max_length=25)
