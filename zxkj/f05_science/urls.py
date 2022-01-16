from django.urls import path
from . import views

app_name = 'science'
urlpatterns = [
    path('', views.index, name='index')
]