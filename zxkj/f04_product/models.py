from django.utils import timezone
from django.db import models


class Product(models.Model):
    """产品的数据表"""
    title = models.CharField(max_length=100, verbose_name='产品名称')
    photo = models.ImageField(upload_to='product/', blank=False, verbose_name="产品图片")
    description = models.TextField(verbose_name="产品描述")
    product_type = models.CharField(max_length=100, verbose_name='产品类型')
    price = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)  # decimal_places小数点的最大位数
    publish_date = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='发布时间')
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    sort = models.CharField(max_length=100, verbose_name='排序')
    state = models.CharField(max_length=100, default="1",verbose_name='状态') # 默认1 有效

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"
        ordering = ('-publish_date', )
