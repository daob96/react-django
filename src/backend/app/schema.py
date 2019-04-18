import graphene
from graphene_django.types import DjangoObjectType
from app.models import Artist, Song, Album

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist

class SongType(DjangoObjectType):
    class Meta:
        model = Song

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


class Query(object):
    all_artists = graphene.List(ArtistType)
    all_songs = graphene.List(SongType)
    all_albums = graphene.List(AlbumType)

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()

    def resolve_all_songs(self, info, **kwargs):
        return Song.objects.select_related('artist','album').all()
