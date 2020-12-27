from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView)
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


class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['favourite_image', 'review', 'rating', 'city', 'country']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def edit_function(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class ReviewDeleteView(DeleteView):
    model = Review
    success_url = '/reviews'

    def edit_function(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

