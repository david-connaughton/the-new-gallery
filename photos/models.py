from django.db import models


class Photo(models.Model):
    """Custom Photo Model"""
    title = models.CharField(max_length=100)
    photographer = models.CharField(max_length=100)
    tag = models.CharField(max_length=20)
    description = models.CharField(max_length=300, null=True, blank=True)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title


