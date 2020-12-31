from django.test import TestCase
from reviews.models import Image


class TestReviewsModel(TestCase):

    def test_review_model(self):
        test_review = Image(image='a new image')
        self.assertEqual(str(test_review), 'a new image')