from django.contrib import admin
from .models import Product,Image,Variety


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'feature')


class VarietyAdmin(admin.ModelAdmin):
    list_display = ('id', 'color')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Image)