from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import SignupForm
from .models import CustomUser as User
from artwork import models as artwork_models

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login') # TODO: redirect to the home page
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/')

def user_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        my_artworks = artwork_models.Artwork.objects.filter(owner=user)
        my_collections = artwork_models.Collection.objects.filter(owner=user)
        collection_data = []
        for collection in my_collections:
            artworks_for_collection = artwork_models.Artwork.objects.filter(collection=collection)
            artworks_count = artworks_for_collection.count()
            collection_dict = {
                'collection': collection,
                'artworks': artworks_for_collection,
                'artworks_count': artworks_count,
            }
            collection_data.append(collection_dict)

        return render(request, 'accounts/profile.html', {'user': user, 'my_artworks': my_artworks, 'my_collections': collection_data})
    else:
        return redirect('accounts:login')

def users_artworks(request, pk):
    if request.user.is_authenticated:
        sort_param = request.GET.get('filter', 'name')  # Get the sorting parameter from the URL query string, defaulting to 'name'
        user = User.objects.get(pk=pk)
        if sort_param == 'name':
            artworks =  artwork_models.Artwork.objects.filter(owner=pk).order_by('title')
        elif sort_param == '-name':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('-title')
        elif sort_param == 'year':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('year')
        elif sort_param == '-year':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('-year')
        elif sort_param == 'artist':
            artworks = artwork_models.Artwork.objects.filter(owner=pk).order_by('artist')
        else:
            artworks = artwork_models.Artwork.objects.filter(owner=pk)


        return render(request, 'accounts/users_artworks.html', {
            'artworks': artworks,
            'user': user
        })
    else:
        return redirect('accounts:login')

def users_collections(request, pk):

    if request.user.is_authenticated:
            sort_param = request.GET.get('filter', 'name')
            if sort_param == 'name':
                collections = artwork_models.Collection.objects.filter(owner=pk).order_by('name')
            elif sort_param == '-name':
                collections = artwork_models.Collection.objects.filter(owner=pk).order_by('-name')
            else:
                collections = artwork_models.Collection.objects.filter(owner=pk)

            collection_data = []
            for collection in collections:
                artworks_for_collection =artwork_models.Artwork.objects.filter(collection=collection)
                artworks_count = artworks_for_collection.count()
                collection_dict = {
                    'collection': collection,
                    'artworks': artworks_for_collection,
                    'artworks_count': artworks_count,
                }
                collection_data.append(collection_dict)

            return render(request, 'accounts/users_collections.html', {'collections': collection_data, 'sort_param': sort_param})
    else:
        return redirect('accounts:login')
