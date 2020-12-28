from django.shortcuts import render


def tours(request):
    return render(request, 'tours/tours.html')

