# Generated by Django 4.0.1 on 2022-01-15 07:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('photo', models.ImageField(blank=True, upload_to='AD/', verbose_name='广告图片')),
                ('url', models.CharField(max_length=500, verbose_name='URL链接')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=1, verbose_name='浏览量')),
                ('sort', models.CharField(max_length=100, verbose_name='排序')),
                ('state', models.CharField(default='1', max_length=100, verbose_name='状态')),
            ],
            options={
                'verbose_name': '广告',
                'verbose_name_plural': '广告列表',
                'ordering': ('-sort', '-publish_date'),
            },
        ),
    ]
