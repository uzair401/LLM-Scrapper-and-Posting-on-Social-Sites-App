from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, SigninForm
from django.http import HttpResponse


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Authenticate and login
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = SigninForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = SigninForm()
    return render(request, 'signin.html', {'form': form})


def signout_view(request):
    logout(request)
    return redirect('home')


def home_view(request):
    return HttpResponse("Home Page")
