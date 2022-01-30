import uuid
from django.db import models

class CommonModels(models.Model):

    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, verbose_name='外部使用的唯一标识')
    sort = models.CharField(max_length=100, verbose_name='排序标识')
    type = models.CharField(max_length=100, verbose_name='分类')
    group = models.CharField(max_length=100, verbose_name='分组')
    state = models.CharField(max_length=100, verbose_name='状态')
    remark = models.CharField(max_length=500, verbose_name='备注')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    deleted_at = models.DateTimeField(null=True, verbose_name='伪删除时间')
    created_by = models.CharField(max_length=100, verbose_name='创建人') 
    updated_by = models.CharField(max_length=100, verbose_name='修改人') 
    deleted_by = models.CharField(max_length=100, verbose_name='伪删除时间') 

class User(CommonModels):

    login_name = models.CharField(max_length=100, unique=True, verbose_name='登录名')
    nickname = models.CharField(max_length=100, verbose_name='昵称')
    email = models.EmailField(max_length=100, verbose_name='邮箱')
    phone = models.CharField(max_length=100, verbose_name='手机')
    avatar = models.CharField(max_length=500, verbose_name='头像信息(URL)')
    password = models.CharField(max_length=100, verbose_name='密码')
    password_salt = models.CharField(max_length=100, verbose_name='密码盐')

class Menu(CommonModels):

    name = models.CharField(max_length=100, verbose_name='名字')
    icon = models.CharField(max_length=500, verbose_name='图标(URL)')
    path = models.CharField(max_length=500, verbose_name='路径')
    level = models.CharField(max_length=100, verbose_name='层级')
    parent = models.ForeignKey('self',blank=True, null=True, related_name='children', on_delete=models.CASCADE, verbose_name='上级的唯一标识')
    #depth = models.IntegerField(default=0)
