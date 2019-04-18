import graphene
import app.schema
from graphene_django.types import DjangoObjectType
from app.models import Artist, Song, Album

class Queries(app.schema.Query,
    graphene.ObjectType
):
    # dummy = graphene.String()
    pass

schema = graphene.Schema(query=Queries)
