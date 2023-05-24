from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Artwork

def detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)

    return render(request, 'artwork/detail.html', {
        'artwork': artwork
    })