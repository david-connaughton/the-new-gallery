"""Inspired by Code Institute Tutorial"""

import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField
from photos.models import Photo


class Order(models.Model):

    EMAIL = "Email Print"
    NO_EMAIL = "Please don't email Print"

    EMAIL_PRINT = (
        (EMAIL, "Email Print"),
        (NO_EMAIL, "Please Don't Email Print"),
    )

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=32, null=False, blank=False)
    street_address_1 = models.CharField(max_length=50, null=False, blank=False)
    street_address_2 = models.CharField(max_length=50, null=True, blank=True)
    county = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=15, null=False, blank=False)
    city = models.CharField(max_length=32, null=False, blank=False)
    country = CountryField(
        blank_label='Country', null=False, blank=False
    )
    date = models.DateField(auto_now_add=True)
    email_print = models.CharField(
        max_length=30, choices=EMAIL_PRINT, default=EMAIL)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    photo = models.ForeignKey(
        Photo, null=False, blank=False,
        on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.photo.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.order.order_number}'
