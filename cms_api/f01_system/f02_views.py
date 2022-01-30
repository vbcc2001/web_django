from django.http import JsonResponse


def index(request):
    data={
        'name':'system-api'
    }
    return JsonResponse(data)