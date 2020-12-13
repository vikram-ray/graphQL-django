import graphene
from graphene_django import DjangoObjectType
from .models import Actor, Director, Movie


class User(DjangoObjectType):
    class Meta:
        model = Actor

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return Actor.objects.all()

schema = graphene.Schema(query=Query)
