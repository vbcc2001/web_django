from django.db import models
# 荣誉
class Award(models.Model):

    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='描述')
    photo = models.ImageField(upload_to='award/', blank=True, verbose_name="图片")
    sort = models.CharField(max_length=100, verbose_name='排序')
    state = models.CharField(max_length=100, default="1",verbose_name='状态') # 默认1 有效

    def __str__(self):
        return self.photo

    class Meta:
        verbose_name = verbose_name_plural = '荣誉资质'
        db_table = 'award'
        ordering = ('-id', )
