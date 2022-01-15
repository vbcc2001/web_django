from django.db import models
# 荣誉
class Award(models.Model):

    title = models.TextField(max_length=500, verbose_name='标题')
    description = models.TextField(max_length=500, verbose_name='描述')
    photo = models.ImageField(upload_to='award/', blank=True, verbose_name="图片")
    sort = models.CharField(max_length=100,  blank=True, verbose_name='排序')
    state = models.CharField(max_length=100, default="1",verbose_name='状态') # 默认1 有效

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '荣誉资质'
        ordering = ('-id', )
