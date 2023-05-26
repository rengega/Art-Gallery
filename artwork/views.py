from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Artwork, Artist, Genre

def detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    related = Artwork.objects.filter(genre=artwork.genre).exclude(pk=pk)

    return render(request, 'artwork/detail.html', {
        'artwork': artwork,
        'related': related
    })

def all_artists(request):
    if request.user.is_authenticated:
        sort_param = request.GET.get('filter', 'name')  # Get the sorting parameter from the URL query string, defaulting to 'name'

        if sort_param == 'name':
            artists = Artist.objects.all().order_by('name')
        elif sort_param == '-name':
            artists = Artist.objects.all().order_by('-name')
        elif sort_param == 'birthday':
            artists = Artist.objects.all().order_by('date_of_birth')
        elif sort_param == '-birthday':
            artists = Artist.objects.all().order_by('-date_of_birth')
        else:
            artists = Artist.objects.all()

        return render(request, 'artwork/all_artists.html', {'artists': artists, 'sort_param': sort_param})
    else:
        return redirect('accounts:login')

def all_artworks(request, ):
    if request.user.is_authenticated:
        sort_param = request.GET.get('filter', 'name')  # Get the sorting parameter from the URL query string, defaulting to 'name'

        if sort_param == 'name':
            artworks = Artwork.objects.all().order_by('title')
        elif sort_param == '-name':
            artworks = Artwork.objects.all().order_by('-title')
        elif sort_param == 'year':
            artworks = Artwork.objects.all().order_by('year')
        elif sort_param == '-year':
            artworks = Artwork.objects.all().order_by('-year')
        elif sort_param == 'artist':
            artworks = Artwork.objects.all().order_by('artist')
        else:
            artworks = Artwork.objects.all()

        return render(request, 'artwork/all_artworks.html', {'artworks': artworks, 'sort_param': sort_param})
    else:
        return redirect('accounts:login')
