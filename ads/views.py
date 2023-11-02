from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *


menu = [
    {'title': 'Последние объявления', 'url_name': 'last_ads'},
    {'title': 'Подобрать VIN', 'url_name': 'select_vin'},
    {'title': 'Фильтр по объявлениям', 'url_name': 'filter_ads'},
    {'title': 'Добавить объявление', 'url_name': 'add_ads'}
]


# def main(request):
#     ad = Ads.objects.all()
#     context = {
#         'menu': menu,
#         'ads': ad,
#         'cat_selected': 0
#     }
#     return render(request, 'ads/main.html', context=context)


class MainPage(ListView):
    paginate_by = 2
    model = Ads
    template_name = 'ads/main.html'
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat_selected'] = 0
        return context


# def show_cat(request, cat_slug):
#     cat = get_object_or_404(Category, slug=cat_slug)
#     ads = Ads.objects.filter(cat_id=cat.id)
#     context = {
#         'menu': menu,
#         'ads': ads,
#         'cat_selected': cat_slug
#     }
#     return render(request, 'ads/main.html', context=context)


class ShowCat(ListView):
    paginate_by = 2
    model = Ads
    template_name = 'ads/main.html'
    context_object_name = 'ads'
    allow_empty = False

    def get_queryset(self):
        return Ads.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat_selected'] = context['ads'][0].cat_id
        return context


# def show_ads(request, ads_slug):
#     ad = get_object_or_404(Ads, slug=ads_slug)
#     context = {
#         'menu': menu,
#         'ads': ad,
#         'cat_selected': ad.cat_id
#     }
#     return render(request, 'ads/show_ad.html', context=context)


class ShowAds(DetailView):
    model = Ads
    template_name = 'ads/show_ad.html'
    slug_url_kwarg = 'ads_slug'
    context_object_name = 'ads'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        #context['cat_selected'] = context['ads'].cat_id
        return context


def last_ads(request):
    context = {
        'menu': menu
    }
    return render(request, 'ads/last_ads.html', context=context)


def select_vin(request):
    context = {
        'menu': menu
    }
    return render(request, 'ads/select_vin.html', context=context)


def filter_ads(request):
    context = {
        'menu': menu
    }
    return render(request, 'ads/filter_ads.html', context=context)


def user_login(request):
    context = {
        'menu': menu
    }
    return render(request, 'ads/login.html', context=context)


def register(request):
    context = {
        'menu': menu
    }
    return render(request, 'ads/register.html', context=context)


# def add_ads(request):
#     if request.method == 'POST':
#         form = AddAdForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddAdForms()
#     context = {
#         'menu': menu,
#         'form': form
#     }
#     return render(request, 'ads/add_ads.html', context=context)


class AddAds(CreateView):
    form_class = AddAdForms
    template_name = 'ads/add_ads.html'
    context_object_name = 'ads'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'ads/register.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'ads/login.html'
    success_url = reverse_lazy('register')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')



def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Хуй тебе, а не страница<h1><h2>Нет такой<h2>')
