"""Inspired by Code Institute Tutorial"""

from django.conf import settings
"""Re-purposed from Code Institute Tutorial"""

from django.shortcuts import get_object_or_404
from photos.models import Photo


def cart_contents(request):
    """A view for Cart Contents"""
    cart_items = []
    total = 0
    photo_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        photo = get_object_or_404(Photo, pk=item_id)
        total += quantity * photo.price
        photo_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'photo': photo,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'photo_count': photo_count,
    }

    return context
