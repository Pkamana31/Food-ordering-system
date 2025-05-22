from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from menu.models import Location, Category, Item, Restaurant, Menu
from .models import Order, OrderedItem

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='customer', email='testmail@example.com', password='mypassword')
        self.location = Location.objects.create(name='California', address='some adress')
        self.category = Category.objects.create(name='Drink')
        self.restaurant = Restaurant.objects.create(name='New Restaurant', location=self.location, phone_number='4343212121', image='some_image.jpg', category=self.category)
        self.menu = Menu.objects.create(restaurant=self.restaurant, category=self.category, name='Drinks', description='Cool drinks')
        self.item = Item.objects.create(name='Coke', description='taste the feelings', price=10.0, menu=self.menu)
        self.order = Order.objects.create(customer=self.user, total_price=10.0, location=self.location)
        self.ordered_item = OrderedItem.objects.create(order=self.order, item=self.item, quantity=1, price=10.0)



    def test_place_order_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('place_order', kwargs={'item_id': self.item.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_confirmation.html')

    def test_reorder_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('reorder', kwargs={'order_id': self.order.id}))
        self.assertEqual(response.status_code, 302)  # redirect after reordering

    def test_order_detail_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('order_detail', kwargs={'order_id': self.order.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_detail.html')
