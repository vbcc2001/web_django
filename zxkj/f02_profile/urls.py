from django.urls import path
from zxkj.f02_profile import views

app_name = 'profile'
urlpatterns = [
    path('', views.index, name='index'),
    path('honor/', views.honor, name='honor'),
]
