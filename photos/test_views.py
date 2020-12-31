from django.test import TestCase


class TestPhotos(TestCase):

    def test_photos_page(self):
        response = self.client.get('/photos/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photos.html')

    def test_photo_details_page(self):
        response = self.client.get('/photos/<1>')
        self.assertNotEqual(response.status_code, 200)

    def test_paginator(self):
        response = self.client.get('/photos/?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photos.html')
