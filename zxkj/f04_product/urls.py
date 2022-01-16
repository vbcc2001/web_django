from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.list, name='list'),
    path('<str:product_type_name>/', views.list, name='list'),
    path('details/<int:id>/', views.details, name="details"),
    path('type', views.types_list, name="type"),
]