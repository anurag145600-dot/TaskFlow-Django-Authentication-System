from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm


def home(request):

    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


def user_login(request):

    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    else:

        form = AuthenticationForm()

    return render(
        request,
        'login.html',
        {'form': form}
    )


def user_logout(request):

    logout(request)

    return redirect('home')