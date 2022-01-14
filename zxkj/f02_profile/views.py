from django.shortcuts import render
from .models import Award

# 企业概况
def index(request):
    return render(request, 'f03_profile/f01_index.html', {'active_menu': 'about', 'sub_menu': 'survey'})

# 荣誉资质
def honor(request):
    awards = Award.objects.all()
    context = {
        'awards': awards,
        'active_menu': 'about',
        'sub_menu': 'honor'
    }
    return render(request, 'f03_profile/f02_honor.html', context)
