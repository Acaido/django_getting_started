from django.contrib import admin

from .models import Group, Discount, Product


admin.site.register(Group)
admin.site.register(Discount)
admin.site.register(Product)
