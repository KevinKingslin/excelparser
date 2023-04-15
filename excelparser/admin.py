from django.contrib import admin
from .models import Product, Variations

# Register your models here.
admin.site.register(Product)
admin.site.register(Variations)