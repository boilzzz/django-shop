from django.contrib import admin
from . import models

@admin.register(models.Products)
class Products(admin.ModelAdmin):
    pass