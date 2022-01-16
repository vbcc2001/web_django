"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .f01_index import views
from . import settings

urlpatterns = [

    path('', views.index, name='index'),
    path('profile/', include('zxkj.f02_profile.urls', namespace='profile')),   # 公司简介
    path('news/', include('zxkj.f03_news.urls', namespace='news')),   # 新闻动态
    path('product/', include('zxkj.f04_product.urls', namespace='product')),   # 产品中心
    path('science/', include('zxkj.f05_science.urls', namespace='science')),   # 产品中心
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)