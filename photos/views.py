from django.shortcuts import render
from .models import Photo


def photos(request):
    """A custom view to render Photo Page"""
    photos = Photo.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'photos/photos.html', context)

