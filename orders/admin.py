from django.contrib import admin

# Register your models here.
from .models import Order, OrderedItem

admin.site.register(Order)
admin.site.register(OrderedItem)