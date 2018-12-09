from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from SICAD.forms import UserRegisterForm
from SICAD.models import Personne

posts = [
    {
        'title': 'Premier Autheur'
    },
    {
        'title': 'Deuxième Auteur'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'sicad/accueil.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('sicad-accueil')
    else:
        form = UserRegisterForm()
    return render(request, 'sicad/register.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('sicad-accueil')
    else:
        form = UserCreationForm()
    return render(request, 'sicad/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    request.session.set_expiry(86400)  # sets the exp. value of the session

                    # profile = Profile.objects.get(user=user.id)
                    # request.session['acces'] = profile.acces
                    request.session['acces'] = 'secretariat'
                    # TODO: fix how to get user access

                    messages.success(request, f'User {username} succesfully logged in!')
                    login(request, user)
            # my_func(request)
            return redirect('sicad-accueil')
    else:
        form = AuthenticationForm()
    return render(request, 'sicad/login.html', {'form': form})


@login_required
def my_func(request):
    messages.success(request, f'Test')


def logout_view(request):
    logout(request)

    messages.success(request, f'User logged out')
    return redirect('sicad-accueil')
