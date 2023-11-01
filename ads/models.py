from django.db import models
from django.urls import reverse


class Category(models.Model):
    name_cat = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name_cat

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Ads(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    year = models.IntegerField(verbose_name='Год')
    price = models.IntegerField(verbose_name='Цена')
    link = models.URLField(verbose_name='Ссылка на объявление')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('ads', kwargs={'ads_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['id']


