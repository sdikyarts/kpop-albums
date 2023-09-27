from django.db import models

from django.contrib.auth.models import User

class Artist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    debut_date = models.DateField(null=True, blank=True)
    disband_date = models.DateField(null=True, blank=True)
    members = models.CharField(max_length=1000, default='')
    former_members = models.CharField(max_length=1000, default='')
    sub_units = models.TextField(default='')
    supporters = models.CharField(max_length=1000, default='')
    description = models.TextField(default='')
    artist_pic = models.ImageField(upload_to='artist_pics/', null=True, blank=True)
    artist_logo = models.ImageField(upload_to='artist_logos/', null=True, blank=True)

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    release_date = models.DateField(null=True, blank=True)
    tracklist = models.CharField(max_length=2000, default='')
    album_cover = models.ImageField(upload_to='album_covers/', null=True, blank=True)
    amount = models.IntegerField(default=0)

# The Item model is no longer needed for artists and albums.
# You can remove it or keep it for other purposes.
