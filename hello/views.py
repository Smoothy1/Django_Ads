from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def main_page(request):
    sneakers = Sneakers.objects.all()
    context = {
        'sneakers': sneakers,
    }
    return render(request, 'hello/main.html', context=context)


def show_sneak(request, sneak_slug):
    sneak = get_object_or_404(Sneakers, slug=sneak_slug)
    context = {
        'sneak': sneak,
    }
    return render(request, 'hello/card.html', context=context)


def order_sneak(request, sneak_slug):
    sneak = get_object_or_404(Sneakers, slug=sneak_slug)
    cur_price = sneak.base_price - sneak.sale
    context = {
        'sneak': sneak,
        'cur_price': cur_price,
    }
    return render(request, 'hello/order.html', context=context)

def about(request):
    return render(request, 'hello/about.html')
