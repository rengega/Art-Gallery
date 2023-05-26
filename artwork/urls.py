from django.urls import path
from . import views

app_name = 'artwork'

urlpatterns = [
    path('<int:pk>', views.detail, name = 'detail'),
    path('all_artists/', views.all_artists, name = 'all_artists'),
    path('all_artworks/', views.all_artworks, name = 'all_artworks'),
    ]