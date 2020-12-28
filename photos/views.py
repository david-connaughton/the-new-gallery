from django.shortcuts import render, get_object_or_404
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


def photo_detail(request, photo_id):
    """A custom view for individual photo detail"""
    photo = get_object_or_404(Photo, pk=photo_id)
    context = {
        'photo': photo,
    }
    return render(request, 'photos/photo_detail.html', context)
