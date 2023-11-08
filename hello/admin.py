from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'model', 'size', 'color', 'get_html_photo', 'base_price', 'cat')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('cat', 'size', 'base_price')
    prepopulated_fields = {'slug': ('name',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(r"<img src='{object.photo.url}' width=50>")


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cat',)
    list_display_links = ('name_cat',)
    search_fields = ('name_cat',)
    prepopulated_fields = {'slug': ('name_cat',)}


admin.site.register(Sneakers, AdsAdmin)
admin.site.register(Category, CatAdmin)
