from django.urls import path, re_path, include
from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('last_ads/', last_ads, name='last_ads'),
    path('select_vin/', select_vin, name='select_vin'),
    path('filter_ads/', filter_ads, name='filter_ads'),
    path('add_ads', AddAds.as_view(), name='add_ads'),
    path('ads/<slug:ads_slug>', ShowAds.as_view(), name='ads'),
    path('category/<slug:cat_slug>', ShowCat.as_view(), name='cat'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
