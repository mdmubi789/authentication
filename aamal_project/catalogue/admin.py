      
from django.contrib import admin

from . models import Category,Product



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'description', 'cat_img')
    
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'price', 'images')
admin.site.register(Product, ProductAdmin)
