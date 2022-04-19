from django.contrib import admin
from .models import Publication
from products.models import Product


class ProductInLine(admin.StackedInline):
    model = Product

class PublicationAdmin(admin.ModelAdmin):
    inlines = [ProductInLine, ]


admin.site.register(Publication, PublicationAdmin)