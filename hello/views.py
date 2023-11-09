from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import *
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


class CreateOrder(CreateView):
    slug_url_kwarg = 'sneak_slug'
    context_object_name = 'sneak'
    form_class = FormOrder
    model = Sneakers
    template_name = 'hello/order.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def about(request):
    return render(request, 'hello/about.html')
