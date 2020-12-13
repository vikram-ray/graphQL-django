import graphene
from graphene_django import DjangoObjectType

from movies import models
class Actor(DjangoObjectType):
    class Meta:
        model = models.Actor


class Director(DjangoObjectType):
    class Meta:
        model = models.Director

class Movie(DjangoObjectType):
    class Meta:
        model = models.Movie


class Query(graphene.ObjectType):
    actor = graphene.List(Actor)
    director = graphene.List(Director)
    movie = graphene.List(Movie)

    def resolve_actor(self, info):
        return models.Actor.objects.all()

    def resolve_director(self, info):
        return models.Director.objects.all()
    
    def resolve_movie(self, info):
        return models.Movie.objects.all()


schema = graphene.Schema(query=Query)
