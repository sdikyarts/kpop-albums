from django.db import models

class Artist(models.Model):
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

    def delete(self, *args, **kwargs):
        # Delete associated image files when an artist is deleted
        if self.artist_pic:
            storage, path = self.artist_pic.storage, self.artist_pic.path
            if storage.exists(path):
                storage.delete(path)

        if self.artist_logo:
            storage, path = self.artist_logo.storage, self.artist_logo.path
            if storage.exists(path):
                storage.delete(path)

        super().delete(*args, **kwargs)

class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    release_date = models.DateField(null=True, blank=True)
    tracklist = models.CharField(max_length=2000, default='')
    album_cover = models.ImageField(upload_to='album_covers/', null=True, blank=True)
    amount = models.IntegerField(default=0)

    def delete(self, *args, **kwargs):
        # Delete associated image file when an album is deleted
        if self.album_cover:
            storage, path = self.album_cover.storage, self.album_cover.path
            if storage.exists(path):
                storage.delete(path)

        super().delete(*args, **kwargs)

# The Item model is no longer needed for artists and albums.
# You can remove it or keep it for other purposes.
