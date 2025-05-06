from django.contrib import admin
from store import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'image', 'price', 'stock',
    list_editable = 'stock',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',

@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = 'user', 'product', 'quantity'
    list_filter = 'user',

@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = 'user', 'product', 'quantity', 'total_price', 'date',
    list_filter = 'user', 'date',
    ordering = '-date',
