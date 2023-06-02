from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
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
        fields = ('name', 'surname', 'date_of_birth', 'bio', 'photo')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Name'}),
            'surname': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Surname'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Date of birth'}),
            'bio': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Bio'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'placeholder': 'Photo'}),
        }


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'placeholder': 'Old password',
            'class': 'w-full py-4 px-6 rounded-xl',
            'autocomplete': 'current-password',
        })
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'New password',
            'class': 'w-full py-4 px-6 rounded-xl',
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Repeat new password',
            'class': 'w-full py-4 px-6 rounded-xl',
        })

    def clean_old_password(self):
        # Custom validation for the old password field
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('The current password is incorrect.')
        return old_password
