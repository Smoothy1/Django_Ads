from django.db import models


class Ads(models.Model):
    mark = models.CharField(max_length=255, verbose_name='Марка')
    model = models.CharField(max_length=255, verbose_name='Модель')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    year = models.IntegerField(verbose_name='Год')
    price = models.IntegerField(verbose_name='Цена')
    city = models.CharField(max_length=255, verbose_name='Город')
    description = models.TextField(max_length=255, verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка на объявление')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
