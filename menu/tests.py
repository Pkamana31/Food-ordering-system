from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Location, Category, Restaurant, Menu, Item

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='customer', email='mytest@example.com', password='mypassword')
        self.location = Location.objects.create(name='California', address='some place')
        self.category = Category.objects.create(name='Drinks')
        self.restaurant = Restaurant.objects.create(name='Cool Restaurant', location=self.location, phone_number='434545459', image='some_image.jpg', category=self.category)
        self.menu = Menu.objects.create(restaurant=self.restaurant, category=self.category, name='Drink', description='coolest coke')
        self.item = Item.objects.create(menu=self.menu, name='coke', description='taste the feeling', price=5.0)

    def test_restaurant_list_view(self):
        response = self.client.get(reverse('restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_list.html')

    def test_restaurant_detail_view(self):
        response = self.client.get(reverse('restaurant_detail', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_detail.html')

    def test_menu_detail_view(self):
        response = self.client.get(reverse('menu_detail', args=[self.menu.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_detail.html')
