from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('', main_page, name='main'),
    path('sneakers/<int:sneak_id>', show_sneak, name='sneak'),
]