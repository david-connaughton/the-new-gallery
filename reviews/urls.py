from django.urls import path
from .views import ReviewListView, ReviewCreateView
from . import views


urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews'),
    path('review/new/', ReviewCreateView.as_view(), name='review_create'),
]
