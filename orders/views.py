from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Order, OrderedItem
from django.contrib.auth.decorators import login_required

@login_required 
def place_order(request, item_id):
    # get the selected item
    item = get_object_or_404(Item, pk=item_id)

    # create an order object
    order = Order.objects.create(customer=request.user, total_price=item.price, location=item.menu.restaurant.location)

    # create an ordered item associated with the order
    ordered_item = OrderedItem.objects.create(order=order, item=item, quantity=1, price=item.price)


    # redirect 
    return render(request, 'order_confirmation.html', {'order': order})

def reorder(request, order_id):
    # retrieve the original order object
    original_order = get_object_or_404(Order, pk=order_id)

    # retrieve the items from the original order
    original_ordered_items = OrderedItem.objects.filter(order=original_order)

    # create a new order with the same items in the old
    new_order = Order.objects.create(
        customer=request.user,
        location=original_order.location,  
        total_price=original_order.total_price,
        status='Pending' 
    )

    # copy the items from the original order to the new
    for ordered_item in original_ordered_items:
        OrderedItem.objects.create(
            order=new_order,
            item=ordered_item.item,
            quantity=ordered_item.quantity,
            price=ordered_item.price
        )

    # redirect 
    return redirect('order_detail', order_id=new_order.id)

def order_detail(request, order_id):
    # retrieve the order object
    order = get_object_or_404(Order, pk=order_id)

    # retrieve the items associated with the order
    ordered_items = OrderedItem.objects.filter(order=order)

    return render(request, 'order_detail.html', {'order': order, 'ordered_items': ordered_items})

