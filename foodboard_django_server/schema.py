import graphene
from graphene_django import DjangoObjectType
from food.schema import schema
class Query(schema.Query,graphene.ObjectType):
    pass

class Mutation(schema.Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)