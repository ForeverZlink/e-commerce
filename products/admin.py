from django.contrib import admin
from django.db import models
from products.models import Product, Type_of_Product, Mark_Product, Imagem_Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
@admin.register(Type_of_Product)
class TypeProductAdmin(admin.ModelAdmin):
    pass
@admin.register(Mark_Product)
class MarkProductAdmin(admin.ModelAdmin):
    pass
@admin.register(Imagem_Product)
class ImagemProductAdmin(admin.ModelAdmin):
    pass