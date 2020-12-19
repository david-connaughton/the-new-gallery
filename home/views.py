from django.shortcuts import render


def home(request):
    """A view to render Home Page"""
    return render(request, 'home/index.html')
