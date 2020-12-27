from django.urls import path
from .views import (
    ReviewListView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView)


urlpatterns = [
    path('', ReviewListView.as_view(), name='reviews'),
    path('review/new/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update',
         ReviewUpdateView.as_view(),
         name='review_update'),
    path('review/<int:pk>/delete',
         ReviewDeleteView.as_view(),
         name='review_delete'),
]
