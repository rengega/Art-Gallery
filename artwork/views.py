from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Artwork, Artist, Genre
from datetime import date
from django.contrib.auth.decorators import login_required
from .forms import NewGenreForm, NewArtistForm, NewArtworkForm

def detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    related = Artwork.objects.filter(genre=artwork.genre).exclude(pk=pk)[0:4]

    return render(request, 'artwork/detail.html', {
        'artwork': artwork,
        'related': related
    })

def artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artworks = Artwork.objects.filter(artist=artist) [0:8]

    birth_year = artist.date_of_birth.year
    start_date = date(birth_year - 50, 1, 1)
    end_date = date(birth_year + 50, 12, 31)

    related = Artist.objects.filter(
        date_of_birth__range=(start_date, end_date)
    ).exclude(pk=pk)[0:4]

    return render(request, 'artwork/artist.html', {
        'artist': artist,
        'related': related,
        'artworks': artworks
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



def artworks_by_artist(request, pk):
    if request.user.is_authenticated:
        artist = get_object_or_404(Artist, pk=pk)
        artworks = Artwork.objects.filter(artist=artist)

        sort_param = request.GET.get('filter', 'name')  # Get the sorting parameter from the URL query string, defaulting to 'name'

        if sort_param == 'name':
            artworks = Artwork.objects.filter(artist=artist).order_by('title')
        elif sort_param == '-name':
            artworks = Artwork.objects.filter(artist=artist).order_by('-title')
        elif sort_param == 'year':
            artworks = Artwork.objects.filter(artist=artist).order_by('year')
        elif sort_param == '-year':
            artworks = Artwork.objects.filter(artist=artist).order_by('-year')
        elif sort_param == 'artist':
            artworks = Artwork.objects.filter(artist=artist).order_by('artist')
        else:
            artworks = Artwork.objects.filter(artist=artist)()

        return render(request, 'artwork/all_artworks.html', {'artworks': artworks, 'sort_param': sort_param})

        return render(request, 'artwork/all_artworks.html', {
            'artworks': artworks,
            'artist': artist
        })
    else:
        return redirect('accounts:login')

@login_required
def new_genre(request):
    if request.method == 'POST':
        form = NewGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/artwork/all_artworks')
    else:
        form = NewGenreForm()
    return render(request, 'artwork/new_genre.html', {
    'form': form,
    'title': 'New Genre'

    })

@login_required
def new_artist(request):
    if request.method == 'POST':
        form = NewArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.photo = form.cleaned_data['photo']
            artist.save()
            return redirect('/artwork/all_artists')
    else:
        form = NewArtistForm()
    return render(request, 'artwork/new_artist.html', {
    'form': form,
    'title': 'New Artist'

    })

@login_required
def new_artwork(request):
    if request.method == 'POST':
        form = NewArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.photo = form.cleaned_data['photo']
            artwork.owner = request.user
            artwork.save()
            return redirect('/artwork/all_artworks')
    else:
        form = NewArtworkForm()
    return render(request, 'artwork/new_artwork.html', {
    'form': form,
    'title': 'New Artwork'

    })