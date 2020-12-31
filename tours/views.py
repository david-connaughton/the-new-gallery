from django.shortcuts import render, redirect, reverse
from .models import Tour
from .forms import TourForm


def tours(request):
    """A view to render Tour Page & Enquiry Form"""
    tour = Tour.objects.all()
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect(reverse('success'))
    form = TourForm
    template = 'tours/tours.html'

    context = {
        'tour': tour,
        'form': form,
    }

    return render(request, template, context)


def success(request):
    """A view to render Success Page"""
    return render(request, 'tours/success.html')
