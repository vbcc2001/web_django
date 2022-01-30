import graphene 
from graphene_django.types import DjangoObjectType
from .f03_models import User,Menu

class UserType(DjangoObjectType):
    class Meta:
        model = User
class MenuType(DjangoObjectType):
    class Meta:
        model = Menu

# 定义动作，类似POST, PUT, DELETE
class UserInput(graphene.InputObjectType):
    login_name = graphene.String(required=True)

class MenuInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    icon = graphene.String(required=True)
    path = graphene.String(required=True)
    parent = graphene.String(required=True)

class CreateUser(graphene.Mutation):
    # api的输入参数
    class Arguments:
        data = UserInput(required=True)

    # api的响应参数
    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    # api的相应操作，这里是create
    def mutate(self, info, data):
        user = User.objects.create(login_name=data['login_name'])
        ok = True
        return CreateUser(user=user, ok=ok)

class CreateMenu(graphene.Mutation):
    # api的输入参数
    class Arguments:
        data = MenuInput(required=True)

    # api的响应参数
    ok = graphene.Boolean()
    menu = graphene.Field(MenuType)

    # api的相应操作，这里是create
    def mutate(self, info, data):
        parent = Menu.objects.get(id=data['parent'])
        data['parent'] = parent
        menu = Menu.objects.create(**data
            # name = data['name'],
            # icon = data['icon'],
            # path = data['path'],
            # parent = data['parent'],            
        )
        ok = True
        return CreateMenu(menu=menu, ok=ok)

# 定义查询，类似GET
class Query(object):
    all_user = graphene.List(UserType)

    def resolve_all_user(self, info, **kwargs):
        # 查询所有SysUser的逻辑
        return User.objects.all()
    
    all_menu = graphene.List(MenuType)

    def resolve_all_menu(self, info, **kwargs):
        # 查询所有SysUser的逻辑
        return Menu.objects.all()