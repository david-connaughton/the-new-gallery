from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Photo


def photos(request):
    """A custom view to render Photo Page with Filter & Pagination"""
    photos = Photo.objects.all()
    query = request.GET.get('q')
    if query:
        photos = Photo.objects.filter(
            Q(tag__icontains=query)
        ).distinct()
    paginator = Paginator(photos, 6)
    page = request.GET.get('page')
    photos = paginator.get_page(page)
    context = {
        'photos': photos,
    }
    return render(request, 'photos/photos.html', context)

