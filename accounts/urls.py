from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm



app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html', authentication_form = LoginForm), name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('my_profile/<int:pk>', views.user_profile, name = 'my_profile'),
    path('users_artworks/<int:pk>/', views.users_artworks, name = 'users_artworks'),
    path('users_collections/<int:pk>/', views.users_collections, name = 'users_collections'),
    path('all_users/', views.all_users, name = 'all_users'),
    ]