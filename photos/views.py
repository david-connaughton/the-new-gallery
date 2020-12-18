from django.shortcuts import render


def photos(request):
    """A view to render Home Page"""
    return render(request, 'photos/photos.html')
