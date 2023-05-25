from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.conf import settings

class Artist(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='artists/', blank=True)

    def __str__(self):
        return self.name + ' ' + self.surname


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Artwork(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    year = models.IntegerField(validators=[MaxValueValidator(2050)])
    photo = models.ImageField(upload_to='artworks/', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
            if not self.owner:
                self.owner = self.artist.user
            super().save(*args, **kwargs)