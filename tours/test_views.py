from django.test import TestCase


class TestTours(TestCase):

    def test_tours_page(self):
        response = self.client.get('/tours/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tours/tours.html')

    def test_tours_success_page(self):
        response = self.client.get('/tours/success/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tours/success.html')



