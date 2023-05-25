from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login') # TODO: redirect to the home page
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})