from django.urls import path
from . import views


urlpatterns = [
    path('', views.tours, name='tours'),
    path('success/', views.success, name='success')
]
