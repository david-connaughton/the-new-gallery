"""Inspired By Code Institute Tutorial"""

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import OrderForm
from .models import Order, OrderLineItem
from photos.models import Photo
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    """A view for checkout page"""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'country': request.POST['country'],
            'email_print': request.POST['email_print'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                photo = Photo.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        photo=photo,
                        quantity=item_data,
                    )
                    order_line_item.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
    else:
        cart = request.session.get('cart', {})
        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address_1': profile.default_street_address_1,
                    'street_address_2': profile.default_street_address_2,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'city': profile.default_city,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """A view for checout success"""
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address_1': order.street_address_1,
                'default_street_address_2': order.street_address_2,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_city': order.city,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    customer_email = order.email
    subject = render_to_string(
            'checkout/confirmation_emails/confirmation_subject.txt',
            {'order': order})
    body = render_to_string(
            'checkout/confirmation_emails/confirmation_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email]
    )
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
    }

    return render(request, template, context)
