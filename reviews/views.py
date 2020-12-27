from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Review


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/reviews.html'
    context_object_name = 'reviews'


class ReviewCreateView(CreateView):
    model = Review
    fields = ['favourite_image', 'review', 'rating', 'city', 'country']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
