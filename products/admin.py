from django.contrib import admin
from .models import Category, Manufactorer, Product, CaroPics

# Register your models here.

admin.site.register(Category)
admin.site.register(Manufactorer)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock',
                    'category', 'latest', 'best', 'available']
    list_editable = ['price', 'stock', 'latest', 'best', 'available']
    list_per_page = 10


admin.site.register(Product, ProductAdmin)


class CaroPicsAdmin(admin.ModelAdmin):

    list_display = ['product', 'image']


admin.site.register(CaroPics)
