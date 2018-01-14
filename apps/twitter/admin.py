from django.contrib import admin

from .models import User, Twit, Tag, Comment

admin.site.register(User)
admin.site.register(Twit)
admin.site.register(Tag)
admin.site.register(Comment)

