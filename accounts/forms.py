from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput( attrs = {
                'placeholder': 'Your username',
                'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget = forms.PasswordInput( attrs = {
                    'placeholder': 'Password',
                    'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'date_of_birth', 'email', 'password1', 'password2')

    username = forms.CharField(widget = forms.TextInput( attrs = {
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
    }))

    name = forms.CharField(widget = forms.TextInput( attrs = {
                'placeholder': 'Name',
                'class': 'w-full py-4 px-6 rounded-xl'
        }))

    surname = forms.CharField(widget = forms.TextInput( attrs = {
                'placeholder': 'Last name',
                'class': 'w-full py-4 px-6 rounded-xl'
        }))

    date_of_birth = forms.CharField(widget = forms.DateInput( attrs = {
                'placeholder': 'Your birthday',
                'class': 'w-full py-4 px-6 rounded-xl'
        }))

    email = forms.CharField(widget = forms.EmailInput( attrs = {
                'placeholder': 'Email',
                'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password1 = forms.CharField(widget = forms.PasswordInput( attrs = {
                'placeholder': 'Password',
                'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget = forms.PasswordInput( attrs = {
                'placeholder': 'Repeat password',
                'class': 'w-full py-4 px-6 rounded-xl'
    }))


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'surname', 'date_of_birth', 'email', 'bio', 'photo')


    name = forms.CharField(widget = forms.TextInput( attrs = {
                'placeholder': 'Name',
                'class': 'w-full py-4 px-6 rounded-xl'
        }))

    surname = forms.CharField(widget = forms.TextInput( attrs = {
                'placeholder': 'Last name',
                'class': 'w-full py-4 px-6 rounded-xl'
        }))

    date_of_birth = forms.CharField(widget = forms.DateInput( attrs = {
                'placeholder': 'Your birthday',
                'class': 'w-full py-4 px-6 rounded-xl'
        }))


    bio = forms.CharField(widget = forms.Textarea( attrs = {
                'placeholder': 'Bio',
                'class': 'w-full py-4 px-6 rounded-xl'
    }))

    photo = forms.ImageField(widget = forms.FileInput( attrs = {
                'placeholder': 'Photo',
                'class': 'w-full py-4 px-6 rounded-xl'
    }))