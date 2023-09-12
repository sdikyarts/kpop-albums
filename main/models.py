from django.db import models
from django.utils.html import format_html

# Create your models here.
class Item(models.Model):
    # Atribut wajib
    name = models.CharField(max_length=255)
    amount = models.IntegerField(default = 0)
    description = models.TextField(default='')

    artist = models.CharField(max_length=255)
    artist_logo = models.URLField(max_length=255, null=True, blank=True)

    company = models.CharField(max_length=255)
    debut_date = models.DateField(null=True, blank=True)
    disband_date = models.DateField(null=True, blank=True)

    members = models.TextField(default='')
    former_members = models.TextField(default='')

    sub_units = models.TextField(default='')
    supporters = models.CharField(max_length=255, default='')

    price = models.IntegerField(default = 0)
    release_date = models.DateField(null=True, blank=True)
    tracklist = models.TextField(default='')

    artist_pic = models.URLField(max_length=255, null=True, blank=True)
    album_cover = models.URLField(max_length=255, null=True, blank=True)

    def artist_pic_display(self):
        if self.artist_pic:
            return format_html('<a href="{}" target="_blank">{}</a>', self.artist_pic, self.artist_pic)
        return ""

    def album_cover_display(self):
        if self.album_cover:
            return format_html('<a href="{}" target="_blank">{}</a>', self.album_cover, self.album_cover)
        return ""
