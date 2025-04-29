from django.contrib import admin
from .models import Product, Category, Characteristic, ProductImage



class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1

class ProductImageInline(admin.TabularInline):  # Можно заменить на StackedInline — будет вертикально
    model = ProductImage
    extra = 1  

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    inlines = [CharacteristicInline, ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)