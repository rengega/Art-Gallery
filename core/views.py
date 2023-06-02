from django.shortcuts import render
from artwork.models import Artwork, Artist, Genre, Collection
from accounts.models import CustomUser as User
from django.db.models import Q
from django.shortcuts import redirect


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



def search(request):
    if request.user.is_authenticated:
        query = request.GET.get('query')
        artworks = Artwork.objects.filter(Q(title__icontains=query) | Q(artist__name__icontains=query) | Q(artist__surname__icontains=query) | Q(genre__name__icontains=query))
        artists = Artist.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
        users = User.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query) | Q(username__icontains=query))
        collections = Collection.objects.filter(name__icontains=query)
        collection_data = []
        for collection in collections:
            artworks_for_collection = Artwork.objects.filter(collection=collection)
            artworks_count = artworks_for_collection.count()
            collection_dict = {
                'collection': collection,
                'artworks': artworks_for_collection,
                'artworks_count': artworks_count,
            }
            collection_data.append(collection_dict)

        results = {
            'query': query,
            'artworks': artworks,
            'artists': artists,
            'collections': collection_data,
            'users': users
        }
        return render(request, 'core/search_results.html', {'results': results})
    else:
        return redirect('accounts:login')
