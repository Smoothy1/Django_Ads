from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('', main_page, name='main'),
    path('sneakers/<slug:sneak_slug>', show_sneak, name='sneak'),
    path('ordering/<slug:sneak_slug>', order_sneak, name='order')
]