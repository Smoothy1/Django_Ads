from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'hello/index.html', {'title': 'Main page'})


def about(request):
    return render(request, 'hello/about.html')
