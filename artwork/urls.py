from django.urls import path
from . import views

app_name = 'artwork'

urlpatterns = [
    path('<int:pk>', views.detail, name = 'detail'),
    path('artist/<int:pk>', views.artist, name = 'artist'),
    path('all_artists/', views.all_artists, name = 'all_artists'),
    path('all_artworks/', views.all_artworks, name = 'all_artworks'),
    path('artworks_by_artist/<int:pk>/', views.artworks_by_artist, name='artworks_by_artist'),
    ]