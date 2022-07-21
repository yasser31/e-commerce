from django.contrib import admin
from .models import Product, Image, Category, Attribute, AttributeValue, ProductVariant


# -------------------------------------------------------

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue


class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]

# ----------------------------------------------------

class ImageInLine(admin.StackedInline):
    model = Image

class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ImageInLine]


admin.site.register(Product)
admin.site.register(AttributeValue)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Attribute, AttributeAdmin)
