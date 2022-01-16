from django.db import models
from django.utils import timezone


class Doc(models.Model):
    """资料下载"""
    title = models.CharField(max_length=40, verbose_name="资料名称")
    file = models.FileField(upload_to='service/doc/', blank=True, verbose_name="文件资料")
    publish_date = models.DateTimeField(max_length=20, default=timezone.now, verbose_name="上传时间")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']
        verbose_name = "资料"
        verbose_name_plural = "资料"
