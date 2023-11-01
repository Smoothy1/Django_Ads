from django.contrib import admin
from .models import *


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'price', 'link', 'photo', 'cat')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('cat', 'year', 'price')
    prepopulated_fields = {'slug': ('name',)}


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat',)
    list_display_links = ('name_cat',)
    search_fields = ('name_cat',)
    prepopulated_fields = {'slug': ('name_cat',)}


admin.site.register(Ads, AdsAdmin)
admin.site.register(Category, CatAdmin)
