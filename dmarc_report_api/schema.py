import graphene

from graphene import relay


class Query(graphene.ObjectType):
    node = relay.Node.Field()

schema = graphene.Schema(query=Query)
