from django.shortcuts import render
from . import send_email
from .forms import ResumeForm
from .models import Ad


def contact(request):
    context = {
        'active_menu': 'employ',
        'sub_menu': 'contact',
    }
    return render(request, 'f07_contact/f01_contact.html', context)


def recruit(request):
    """人才招聘页面"""
    AdList = Ad.objects.all().order_by('-publish_date')
    if request.method == 'POST':
        resumeForm = ResumeForm(data=request.POST, files=request.FILES)
        if resumeForm.is_valid():
            resumeForm.save()
            contact = {
                'AdList': AdList,
                'sub_menu': 'recruit',
            }
            return render(request, 'f07_contact/f03_recruit_success.html')
    else:
        resumeForm = ResumeForm()
    contact = {
        'AdList': AdList,
        'sub_menu': 'recruit',
        'resumeForm': resumeForm,
    }
    return render(request, 'f07_contact/f02_recruit.html', contact)


# 监听发送邮件
# send_email.before_save_resume
# send_email.post_save_resume

