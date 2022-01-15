from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('<str:news_type>/', views.news, name='list'),
    path('detail/<int:id>/', views.details, name='detail'),
]