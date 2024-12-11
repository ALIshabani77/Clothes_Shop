from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Coupon)


class ProductImageAdmin(admin.StackedInline):
    model=ProductImage



class ProductAdmin(admin.ModelAdmin):
    list_display=['products_name','price']
    inlines=[ProductImageAdmin]

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display=['color_name','price']
    model=ColorVariant

@admin.register(SizeVarient)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display=['size_name','price']
    model=SizeVarient



admin.site.register(Products,ProductAdmin)

admin.site.register(ProductImage)