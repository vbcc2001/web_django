from django import forms
from django.utils.safestring import mark_safe
from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'sex', 'person_id', 'email', 'birth', 'edu', 'school', 'major', 'experience', 'position', 'photo')
        edu_list = (
            ('大专', '大专'),
            ('本科', '本科'),
            ('研究生', '研究生'),
            ('博士', '博士'),
            ('其它', '其它'),
        )
        widgets = {
            'edu': forms.Select(choices=edu_list),
            'photo': forms.FileInput(),
        }