from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Menu, Item, Category, Location, Restaurant

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

def menu_detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'menu_detail.html', {'menu': menu})