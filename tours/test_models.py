from django.test import TestCase
from tours.models import Tour


class TestToursModel(TestCase):

    def test_model_field_works(self):
        test_tour = Tour(tour='A New Tour')
        self.assertEqual(str(test_tour), 'A New Tour')
