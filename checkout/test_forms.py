from django.test import TestCase
from checkout.forms import OrderForm


class TestOrderForm(TestCase):

    def test_order_form(self):
        form = OrderForm({
            'order_number': '7073BE73A5F8497AB1140DC2AEED9A30',
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'county': 'County',
            'city': 'City',
            'postcode': 'Postcode',
            'date': 'Dec. 26, 2020'
        })
        self.assertFalse(form.is_valid())
