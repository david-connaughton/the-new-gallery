"""Custom Model"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tour(models.Model):
    IRELAND = 'Wild Atlantic Way'
    FRANCE = 'French Riviera'
    JULY = 'July'
    AUGUST = 'August'
    ANALOGUE = 'Analogue'
    DIGITAL = 'Digital'
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    PROFESSIONAL = 'Professional'
    NONE = 'None'
    VEGETARIAN = 'Vegetarian'
    VEGAN = 'VEGAN'
    COUNTRY_CHOICES = (
        (IRELAND, 'Wild Atlantic Way'),
        (FRANCE, 'French Riviera')
    )
    DATE_CHOICES = (
        (JULY, 'July'),
        (AUGUST, 'August')
    )
    CAMERA_CHOICES = (
        (ANALOGUE, 'Analogue'),
        (DIGITAL, 'Digital')
    )
    SKILL_CHOICES = (
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (PROFESSIONAL, 'Professional')
    )
    DIET_CHOICES = (
        (NONE, 'None'),
        (VEGETARIAN, 'Vegetarian'),
        (VEGAN, 'Vegan')
    )
    tour = models.CharField(
           choices=COUNTRY_CHOICES, max_length=20, default=IRELAND)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_preference = models.CharField(
                      choices=DATE_CHOICES, max_length=20, default=JULY)
    analogue_or_digital = models.CharField(
                          choices=CAMERA_CHOICES,
                          max_length=20, default=ANALOGUE)
    skill_level = models.CharField(choices=SKILL_CHOICES,
                                   max_length=20, default=BEGINNER)
    dietary_requirements = models.CharField(
                           choices=DIET_CHOICES, max_length=20, default=NONE)
    any_comments = models.TextField(
        max_length=200, null=False, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tour
