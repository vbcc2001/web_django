from django.shortcuts import render
from django.shortcuts import HttpResponse


from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(1)  # 单位：秒数，这里指缓存 15 分钟
def index(request):
    # 返回结果
    return render(request, 'f02_index/f01_index.html')
