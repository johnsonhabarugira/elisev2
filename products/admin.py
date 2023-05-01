from django.contrib import admin
from . models import Car, Make, Model, PartCategory, Part
admin.site.register(Car)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(PartCategory)
admin.site.register(Part)