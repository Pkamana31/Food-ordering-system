from django.contrib import admin

# Register your models here.
from .models import Location, Category, Restaurant, Menu, Item

list_items = [Location, Category, Restaurant, Menu, Item
]

for item in list_items:
    admin.site.register(item)