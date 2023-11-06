from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('', mainPage, name='main'),
    path('load_ads/', load, name='load')
]