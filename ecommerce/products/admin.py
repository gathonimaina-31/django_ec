# products/admin.py

from django.contrib import admin
from .models import Category, Product

# Register Category (makes it easy to create categories in the admin panel)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    fields = ('name', 'category', 'price', 'description', 'image') # To show the image field




