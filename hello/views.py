from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, 'hello/base.html')


def about(request):
    return render(request, 'hello/about.html')
