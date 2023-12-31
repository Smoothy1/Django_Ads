from django.contrib import admin
from django.urls import path, re_path, include
from hello import views
from ads.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('captcha/', include('captcha.urls')),
    re_path(r'^about', views.about, name='about'),
    path('', include('ads.urls')),
    path('drom/', include('drom.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ]+urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found

