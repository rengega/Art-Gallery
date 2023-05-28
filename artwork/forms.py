from django import forms
from .models import Artwork, Artist, Genre, Collection
from accounts.models import CustomUser as User

class NewGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Genre name'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Genre description'}),
        }

class NewArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'surname', 'bio', 'date_of_birth', 'photo']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artist name'}),
            'surname': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artist surname'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artist date of birth'}),
            'bio': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Biography'}),
            'photo': forms.FileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artist photo'}),
        }

class NewArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['artist', 'genre', 'title', 'description', 'year', 'photo']

        widgets = {
            'artist': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artist'}),
            'genre': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Genre'}),
            'title': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artwork title'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artwork description'}),
            'year': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artwork year'}),
            'photo': forms.FileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Artwork photo'}),
        }

class NewCollectionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner')
        super().__init__(*args, **kwargs)
        self.fields['artworks'] = forms.ModelMultipleChoiceField(
            #none or blank
            queryset=Artwork.objects.filter(owner=owner, collection=None),
            widget=forms.CheckboxSelectMultiple(attrs={'class': 'scrollable-checkbox ', 'placeholder': 'Available Artworks'}),
            required=False
        )

    class Meta:
        model = Collection
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Collection name'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Collection description'}),
        }


class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'year', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }