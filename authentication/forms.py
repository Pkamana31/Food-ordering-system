from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']
        labels = {
            'phone_number': 'Phone Number',
            'address': 'Address',
        }
