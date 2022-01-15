from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class News(models.Model):
    """添加新闻模块"""
    NEWS_TYPE = (
        ('企业要闻', '企业要闻'),
        ('行业新闻', '行业新闻'),
        ('通知公告', '通知公告'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    description = RichTextField(default='', verbose_name='内容')
    # description = UEditorField(u'内容', default='', width=950, height=280, imagePath='news/images/', filePath='news/files/')
    news_type = models.CharField(choices=NEWS_TYPE, max_length=50, verbose_name='新闻类型')
    photo = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="图片")
    publish_date = models.DateTimeField(max_length=20, default=timezone.now, verbose_name='发布时间')
    views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    sort = models.CharField(max_length=100, verbose_name='排序')
    state = models.CharField(max_length=100, default="1",verbose_name='状态') # 默认1 有效
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻列表'
        ordering = ['-publish_date']
