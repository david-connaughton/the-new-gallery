"""Custom Model"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField
from django.urls import reverse


class Image(models.Model):
    class Meta:
        verbose_name_plural = 'Images'
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.image


class Review(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING_CHOICES = (
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5),
    )
    favourite_image = models.ForeignKey(
        'Image', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(
        blank_label='Country', null=False, blank=False
    )
    review = models.TextField(max_length=200, null=False, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(choices=RATING_CHOICES, default=ONE)

    def __str__(self):
        return self.review

    def get_absolute_url(self):
        return reverse('reviews')
