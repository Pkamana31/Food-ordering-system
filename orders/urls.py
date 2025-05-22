from django.urls import path
from . import views

urlpatterns = [
    path('place_order/<int:item_id>/', views.place_order, name='place_order'),
    path('reorder/<int:order_id>/', views.reorder, name='reorder'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
]
