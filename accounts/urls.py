from django.urls import path
from django.contrib.auth import views as auth_views
from . views import signup
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html', authentication_form = LoginForm), name = 'login'),
    ]