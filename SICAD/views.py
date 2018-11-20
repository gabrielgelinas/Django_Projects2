from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
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


def register(request):
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
