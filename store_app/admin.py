from django.contrib import admin
from .models import Category, Product


#class ProductAdmin:
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)