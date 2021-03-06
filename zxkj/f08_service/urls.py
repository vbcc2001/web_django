from django.urls import path
from . import views,face_detect

app_name = 'service'
urlpatterns = [
    path('doc/download/', views.doc_list, name='download'),  # 资料下载页面
    path('doc/<int:id>/', views.doc, name='doc'),  # 资料下载
    path('platform/', views.platform, name='platform'),  # 人脸识别开放平台
    # path('platform/face_detect', face_detect.face_detect, name='face_detect'),  #人脸检测Demo
]