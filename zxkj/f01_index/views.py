from django.shortcuts import render
from django.views.decorators.cache import cache_page


from django.db.models import Q
from .models import AD
from zxkj.f03_news.models import News
from zxkj.f04_product.models import Product
# from aboutApp.models import AboutUs



# Create your views here.
@cache_page(1)  # 单位：秒数，这里指缓存 15 分钟
def index(request):

    # 广告列表
    adList = AD.objects.filter(state='1').order_by('-sort','-publish_date')[:3]
    # 新闻展报
    newList = News.objects.filter(~Q(news_type='通知公告')).order_by('-publish_date')
    postList = set()
    postNum = 0
    for s in newList:
        if s.photo:
            postList.add(s)
            postNum += 1
        if postNum == 3:  # 只截取最近的3个展报
            break
    # 新闻列表
    if (len(newList) > 7):
        newList = newList[0:7]
    # 通知公告
    noteList = News.objects.all().filter(Q(news_type='通知公告')).order_by('-publish_date')
    if (len(noteList) > 7):
        noteList = noteList[0:7]
    # 产品中心
    productList = Product.objects.all().order_by('-views')
    if (len(productList) > 4):
        productList = productList[0:4]
    # 返回结果
    return render(request, 'f02_index/f01_index.html',{
        'active_menu': 'home',
        'adList': adList,
        'newList': newList,
        'postList': postList,
        'noteList': noteList,
        'productList': productList,
    })
