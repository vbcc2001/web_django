from django.urls import path
from . import f02_views as views


urlpatterns = [
    path('',views.index,name='index'),
]