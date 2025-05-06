from django.contrib import admin
from store import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'image', 'price', 'stock'

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
