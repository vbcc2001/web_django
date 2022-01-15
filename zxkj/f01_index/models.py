from django.db import models
from django.utils import timezone
# Create your models here.

class AD(models.Model):

    title = models.CharField(max_length=100, verbose_name='标题')
    photo = models.ImageField(upload_to='ad/', verbose_name="广告图片")
    url = models.CharField(max_length=500, verbose_name="URL链接")
    publish_date = models.DateTimeField(max_length=20, default=timezone.now, verbose_name="发布时间")
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    sort = models.CharField(max_length=100, verbose_name='排序')
    state = models.CharField(max_length=100, default="1",verbose_name='状态') # 默认1 有效

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "广告"
        verbose_name_plural = "广告列表"
        ordering = ('-sort', '-publish_date')

