from django.shortcuts import render
from django.views.decorators.cache import cache_page

from .models import AD

# Create your views here.
@cache_page(1)  # 单位：秒数，这里指缓存 15 分钟
def index(request):

    # 广告列表
    adList = AD.objects.filter(state='1').order_by('-sort','-publish_date')[:3]
    # 返回结果
    return render(request, 'f02_index/f01_index.html',{
        'adList': adList,
    })
