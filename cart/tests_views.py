from django.test import TestCase


class TestCart(TestCase):

    def test_cart_page(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
