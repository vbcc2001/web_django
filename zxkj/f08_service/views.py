from django.core.paginator import Paginator
from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.encoding import escape_uri_path
from .models import Doc

def doc_list(request):
    doc_list = Doc.objects.all().order_by('-publish_date')
    p = Paginator(doc_list, 5)
    if p.num_pages <= 1:
        page_data = ''
    else:
        page = int(request.GET.get('page', 1))
        doc_list = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
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
    return render(
        request, 'f08_service/f01_doc_list.html', {
            'active_menu': 'service',
            'doc_list': doc_list,
            'page_data': page_data,
        })


def doc(request, id):
    """下载文件"""
    doc = get_object_or_404(Doc, id=id)
    # 获取文件的名字
    file_name = str(doc.file).split('/')[-1]
    # 获取文件的路径
    file_path = '%s%s' % (os.getcwd(),doc.file.url)
    # 将下载文件分批次写入本地磁盘，先不将他们载入文件内存，读取文件，以512B为单位构建迭代器
    response = StreamingHttpResponse(read_file(file_path, 512))
    # 作为文件直接下载到本机，用户再用软件打开
    response['Content-Type'] = 'application/octet-stream'
    # 规定文件名的下载格式，在文件名为中文时，要加上escape_uri_path
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(escape_uri_path(file_name))
    return response


def platform(request):
    return render(request, 'f08_service/f02_plat_form.html', {
        'active_menu': 'service',
    })

def read_file(file_name, size):
    """分批读取文件"""
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c  # 生成器，相当于一个特殊的迭代器，当运行到这个语句的时候会保存当前的对象；下次再运行到这里的时候会接着上次的对象继续运行。
            else:
                break

