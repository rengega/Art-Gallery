from django.urls import path
from . import views

app_name = 'artwork'

urlpatterns = [
    path('<int:pk>', views.detail, name = 'detail'),
    path('artist/<int:pk>', views.artist, name = 'artist'),
    path('all_artists/', views.all_artists, name = 'all_artists'),
    path('all_artworks/', views.all_artworks, name = 'all_artworks'),
    path('artworks_by_artist/<int:pk>/', views.artworks_by_artist, name='artworks_by_artist'),
    path('new_genre/', views.new_genre, name = 'new_genre'),
    path('new_artist/', views.new_artist, name = 'new_artist'),
    path('new_artwork/', views.new_artwork, name = 'new_artwork'),
    path('edit_artwork/<int:pk>/', views.edit_artwork, name = 'edit_artwork'),
    path('new_collection/', views.new_collection, name = 'new_collection'),
    path('edit_collection/<int:pk>/', views.edit_collection, name = 'edit_collection'),
    path('all_collections/', views.all_collections, name = 'all_collections'),
    path('collection/<int:pk>', views.collection, name = 'collection'),
    path('delete_artwork/<int:pk>', views.delete_artwork, name = 'delete_artwork'),
    path('delete_collection/<int:pk>/<str:delete_artworks>', views.delete_collection, name = 'delete_collection'),
    ]