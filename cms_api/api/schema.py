
# 总的schema入口
import graphene
import f01_system.f04_schema

class Query(f01_system.f04_schema.Query, graphene.ObjectType):
    # 总的Schema的query入口
    pass

class Mutations(graphene.ObjectType):
    # 总的Schema的mutations入口
    create_user = f01_system.f04_schema.CreateUser.Field()
    create_menu = f01_system.f04_schema.CreateMenu.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)