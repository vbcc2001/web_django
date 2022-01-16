from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db import connection
from django.http import JsonResponse

def list(request, product_type_name = None):
    if product_type_name is None:
        product_list = Product.objects.order_by('-publish_date') 
    else:
        product_list = Product.objects.filter(product_type=product_type_name).order_by('-publish_date')
    product_type_list = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT product_type FROM f04_product_product group by product_type")
        row = cursor.fetchall()
        print(row)
        for item in row:
            product_type_list.append(item[0])
    # 分页处理
    # 每页显示2条数据
    p = Paginator(product_list, 5)
    if p.num_pages <= 1:
        page_data = ''
    else:
        # 得到当前页，默认为1
        page = int(request.GET.get('page', 1))
        # 对页数进行分页
        product_list = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages   # 总页数
        page_range = p.page_range   # 页数迭代
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        page_data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }

    context = {
        'active_menu': 'products',
        'product_type_name': product_type_name,
        'product_list': product_list,
        'page_data': page_data,
        'product_type_list':product_type_list
    }
    return render(request, 'f05_product/f01_list.html', context)


def details(request, id):
    """产品的详情页"""
    product = get_object_or_404(Product, id=id)  # 按id进行查找，没有时返回404
    product.views += 1  # 浏览数加1
    product.save()
    return render(request, 'f05_product/f02_details.html', {
        'active_menu': 'products',
        'product': product,
    })

def types_list(request):
    product_type_list = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT product_type FROM f04_product_product group by product_type")
        row = cursor.fetchall()
        print(row)
        for item in row:
            product_type_list.append(item[0])
    data = {"product_type_list":product_type_list}
    return JsonResponse(data)