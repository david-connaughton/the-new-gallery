from django.test import TestCase
from photos.models import Photo


class TestPhotoModel(TestCase):

    def test_photo_model(self):
        test_photo = Photo.objects.create(title='Monday', price=100.00)
        self.assertEqual(str(test_photo), 'Monday', 100.00)
