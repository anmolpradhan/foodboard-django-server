from django.contrib import admin
from .models import Category, Food, SizeGroup, Size, Variant

# Register your models here.
models = [Category, Food, SizeGroup, Size, Variant]
admin.site.register(models)
