from django.contrib import admin

from .f03_models import Menu

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   {'fields': ['name']}),
        ('路径', {'fields': ['path']}),
        ('图标', {'fields': ['icon']}),
        ('父级', {'fields': ['parent']}),
    ]

admin.site.register(Menu, QuestionAdmin)

