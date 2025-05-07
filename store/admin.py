from django.contrib import admin
from .models import Product, Category, Characteristic, ProductImage, Order



class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    extra = 1

class ProductImageInline(admin.TabularInline):  # Можно заменить на StackedInline — будет вертикально
    model = ProductImage
    extra = 1  

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    inlines = [CharacteristicInline, ProductImageInline]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone')
    list_editable = ('is_processed',)

admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)