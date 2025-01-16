import graphene
from graphene_django import DjangoObjectType
from .models import Client

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = (
            'id',
            'first_name',
            'last_name',
            'city'
        )


class Query(graphene.ObjectType):
    all_clients = graphene.List(ClientType)


schema = graphene.Schema(query=Query)