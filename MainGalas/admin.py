from django.contrib import admin
from .models import Category, Product, ProductImg

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImg)
