from django.contrib import admin
from .models import Artwork, Artist, Genre, Collection

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Artwork)
admin.site.register(Collection)
# Register your models here.
