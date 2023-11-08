from django.db import models
from django.urls import reverse


class Sneakers(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    model = models.CharField(max_length=255, verbose_name='Модель')
    size = models.IntegerField(verbose_name='Размер')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    base_price = models.IntegerField(verbose_name='Базовая цена')
    sale = models.IntegerField(verbose_name='Скидка')
    stock = models.BooleanField(verbose_name='Наличие')
    description = models.TextField(max_length=500, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ads', kwargs={'sneak_id': self.pk})


class Category(models.Model):
    name_cat = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name_cat
