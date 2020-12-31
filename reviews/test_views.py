from django.test import TestCase


class TestReviews(TestCase):

    def test_reviews_page(self):
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    def test_reviews_form_page(self):
        response = self.client.get('/reviews/review/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_form.html')

    def test_review_delete(self):
        response = self.client.get('/reviews/review/7/delete/')
        self.assertNotEqual(response.status_code, 200)