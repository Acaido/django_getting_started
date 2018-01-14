from django.contrib import admin

from .models import Performer, Album, Genre, Band, Track, BandRole
from .models import PerformerBand

admin.site.register(PerformerBand)

admin.site.register(Performer)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Track)
admin.site.register(BandRole)
