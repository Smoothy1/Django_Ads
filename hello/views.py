from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def main_page(request):
    sneakers = Sneakers.objects.all()
    context = {
        'sneakers': sneakers,
    }
    return render(request, 'hello/main.html', context=context)


def show_sneak(request, sneak_id):
    sneak = get_object_or_404(Sneakers, pk=sneak_id)
    context = {
        'sneak': sneak,
    }
    return render(request, 'hello/card.html', context=context)

def about(request):
    return render(request, 'hello/about.html')
