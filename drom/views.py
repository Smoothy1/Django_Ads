from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
import re
from .models import *


def mainPage(request):
    return render(request, 'drom/main.html')


def pars():
    ads_list = []
    for i in range(1, 5):
        url = f"https://auto.drom.ru/all/page{i}/"
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        all_ads = soup.find_all('a', class_='css-xb5nz8 e1huvdhj1')
        if all_ads:
            for ads in all_ads:
                name_url = ads.get('href')
                title = ads.find('div', class_='css-1wgtb37 e3f4v4l2').text
                name = title.split(',')[0]
                mark = name.split()[0]
                model = ' '.join(name.split()[1:])
                year = title.split(',')[1].replace(' ', '')
                descr = ads.find('div', class_='css-1fe6w6s e162wx9x0').text
                price1 = ads.find('span', class_='css-46itwz e162wx9x0').text
                price = int(''.join(re.findall('\d', price1)))
                city = ads.find('span', class_='css-1488ad e162wx9x0').text
                if ads.find('img', class_='css-9w7beg evrha4s0'):
                    photo = ads.find('img', class_='css-9w7beg evrha4s0').get('data-src')
                else:
                    photo = None
                ads_dict = {
                    'name_url': name_url,
                    'name': name,
                    'mark': mark,
                    'model': model,
                    'year': year,
                    'descr': descr,
                    'price': price,
                    'city': city,
                    'photo': photo
                }
                ads_list.append(ads_dict)
    return ads_list


def load(request):
    ads_l = pars()
    for obj in ads_l:
        ads = Ads()
        ads.mark = obj['mark']
        ads.model = obj['model']
        ads.slug = obj['name_url'].split("/")[-1]
        ads.year = obj['year']
        ads.price = obj['price']
        ads.city = obj['city']
        ads.description = obj['descr']
        ads.link = obj['name_url']
        ads.photo = obj['photo']
        adss = Ads.objects.all()
        if not adss.filter(slug=ads.slug):
            ads.save()
    ad = Ads.objects.all()
    context = {
        'ads': ad
    }
    return render(request, 'drom/load.html', context=context)
