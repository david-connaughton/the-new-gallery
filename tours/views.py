from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Tour
from .forms import TourForm


def tours(request):
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
    return render(request, 'tours/success.html')
