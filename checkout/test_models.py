from django.test import TestCase
from checkout.models import Order


class TestCheckoutModel(TestCase):

    def test_checkout_model(self):
        test_checkout = Order(order_number='123', full_name='alan')
        self.assertEqual(str(test_checkout), '123', 'alan')
