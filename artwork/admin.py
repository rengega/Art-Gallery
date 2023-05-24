from django.contrib import admin
from .models import Artwork, Artist, Genre

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Artwork)
# Register your models here.
