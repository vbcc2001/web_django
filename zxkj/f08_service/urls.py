from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    path('doc/download/', views.doc_list, name='download'),  # 资料下载页面
    path('doc/<int:id>/', views.doc, name='doc'),  # 资料下载
    path('facedetect/', views.facedetect, name='facedetect'),  # 本地人脸检测api
    path('facedetect/demo', views.facedetectDemo, name='facedetectDemo'),  #网络api人脸检测
    path('platform/', views.platform, name='platform'),  # 人脸识别开放平台
]