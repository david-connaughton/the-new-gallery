from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('default_phone_number',
                  'default_street_address_1',
                  'default_street_address_2',
                  'default_county',
                  'default_postcode',
                  'default_city',
                  'default_country',)
