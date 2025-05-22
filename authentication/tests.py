from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.signin_url = reverse('signin')
        self.view_profile_url = reverse('view_profile')
        self.edit_profile_url = reverse('edit_profile')
        self.user = User.objects.create_user(username='customer', password='mypassword')
        self.profile = Profile.objects.create(user=self.user, phone_number='32435454', address='MY Address')

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post(self.register_url, {
            'username': 'newcustomer',
            'email': 'newcustomer@cust.com',
            'password1': 'mypassword',
            'password2': 'mypassword',
            'phone_number': '324545446',
            'address': 'New Address'
        })
        self.assertEqual(response.status_code, 302)  

    def test_signin_view(self):
        response = self.client.get(self.signin_url)
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post(self.signin_url, {
            'username': 'customer',
            'password': 'mypassword'
        })
        self.assertEqual(response.status_code, 302)  

    def test_view_profile_view(self):
        self.client.login(username='customer', password='mypassword')
        response = self.client.get(self.view_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_edit_profile_view(self):
        self.client.login(username='customer', password='mypassword')
        response = self.client.get(self.edit_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_profile.html')
        
        response = self.client.post(self.edit_profile_url, {
            'phone_number': '987654321',
            'address': 'Updated Address'
        })
        self.assertEqual(response.status_code, 302)  

class TestForms(TestCase):

    def test_profile_form(self):
        form_data = {
            'phone_number': '323232323',
            'address': 'My address'
        }
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid(self):
        # incalid data
        form_data = {
            'phone_number': '',
            'address': ''
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())
