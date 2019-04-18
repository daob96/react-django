from __future__ import unicode_literals
from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'

class Album(models.Model):
    name = models.CharField(max_length=100)
    date_published = models.DateField()

    def __str__(self):
        return f'{self.name} {self.date_published}'


class Song(models.Model):
    name = models.CharField(max_length=100)
    date_published = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.date_published} {self.artist} {self.album}'
