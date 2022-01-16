# Generated by Django 4.0.1 on 2022-01-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f01_index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='photo',
            field=models.ImageField(upload_to='ad/', verbose_name='广告图片'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览量'),
        ),
    ]