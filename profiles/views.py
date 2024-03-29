from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order 
from reviews.models import Review


def profile(request):
    """A view for user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    reviews = Review.objects.filter(user=request.user)

    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'reviews': reviews,
        'on_profile_page': True,
    }
    return render(request, template, context)
