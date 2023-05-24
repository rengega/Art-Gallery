from django.shortcuts import render
from artwork.models import Artwork, Artist, Genre

def index(request):
    artworks = Artwork.objects.all()[0:4]
    artists = Artist.objects.all()
    genres = Genre.objects.all()


    return render(request, 'core/index.html', {
        'artworks': artworks,
        'artists': artists,
        'genres': genres
    })


def contact(request):
    return render(request, 'core/contact.html')

