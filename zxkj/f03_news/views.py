from django.core.paginator import Paginator
from django.shortcuts import render
# from pyquery import PyQuery as pq
from .models import News

def news(request, news_type):
    """新闻动态的动态选择"""
    sub_menu = news_type
    if news_type == 'company':
        news_name = "企业要闻"
    elif news_type == 'industry':
        news_name = '行业新闻'
    elif news_type == 'notice':
        news_name = '通知公告'
    else:
         news_name = ''   

    # 从数据库中取出数据
    new_list = News.objects.filter(news_type=news_name).order_by('-publish_date')
    # 分页处理
    p = Paginator(new_list, 4)
    # 获取当前页数
    page = int(request.GET.get('page', 1))
    # 根据当前页码，返回数据
    news_list = p.page(page)

    context = {
        'active_menu': 'news',
        'sub_menu': news_type,
        'news_list': news_list,
        'news_name': news_name
    }

    return render(request, 'f04_news/f01_list.html', context)


def details(request, id):
    news = News.objects.get(id=id)
    news.views += 1
    news.save()
    context = {
        'active_menu': 'news',
        'mynew': news,
    }
    return render(request, 'f04_news/f02_details.html', context)





