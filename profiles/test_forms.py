from django.test import TestCase
from profiles.forms import UserProfileForm


class TestProfileForm(TestCase):

    def test_profile_form(self):
        form = UserProfileForm({'phone_number': '0000',
                                'street_address_1': '1 Main Street',
                                'street_address_2': 'Main Road',
                                'county': 'Dublin',
                                'postcode': '00000',
                                'city': 'Dublin',
                                'country': 'Ireland'
                                })
        self.assertTrue(form.is_valid())
