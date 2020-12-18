from django.shortcuts import render
from django.db.models import Q
from .models import Photo


def photos(request):
    """A custom view to render Photo Page"""
    photos = Photo.objects.all()
    query = request.GET.get('q')
    if query:
        photos = Photo.objects.filter(
            Q(tag__icontains=query)
        ).distinct()
    context = {
        'photos': photos,
    }
    return render(request, 'photos/photos.html', context)

