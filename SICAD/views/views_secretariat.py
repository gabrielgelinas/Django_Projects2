from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from SICAD.models import ClasseForm, ProgrammeForm, SujetForm, UserPersonneForm
from django.contrib import messages


def home(request):
    return render(request, 'sicad/secretariat.html')


def create_user_form(request):
    if request.method == 'POST':
        user_form = UserPersonneForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Programme {username} created!')
            return redirect('sicad-secretariat')
    else:
        user_form = UserPersonneForm()
    return render(request, 'sicad/secretariat.html', {'form': user_form, 'type': 'create_user_form'})


def create_program(request):
    if request.method == 'POST':
        programme_form = ProgrammeForm(request.POST)
        if programme_form.is_valid():
            programme_form.save()
            description = programme_form.cleaned_data.get('description')
            messages.success(request, f'Programme {description} created!')
            return redirect('sicad-secretariat')
    else:
        programme_form = ProgrammeForm()
    return render(request, 'sicad/secretariat.html', {'form': programme_form, 'type': 'programme_form'})


def create_sujet(request):
    if request.method == 'POST':
        sujet_form = SujetForm(request.POST)
        if sujet_form.is_valid():
            sujet_form.save()
            code_sujet = sujet_form.cleaned_data.get('codeSujet')
            messages.success(request, f'Programme {code_sujet} created!')
            return redirect('sicad-secretariat')
    else:
        sujet_form = SujetForm()
    return render(request, 'sicad/secretariat.html', {'form': sujet_form, 'type': 'sujet_form'})


def create_classe(request):
    if request.method == 'POST':
        class_form = ClasseForm(request.POST)
        if class_form.is_valid():
            class_form.save()
            sujet = class_form.cleaned_data.get('Sujet')
            code_classe = class_form.cleaned_data.get('codeClasse')
            messages.success(request, f'Classe {code_classe} - {sujet} created !')
            return redirect('sicad-secretariat')
    else:
        class_form = ClasseForm()
    return render(request, 'sicad/secretariat.html', {'form': class_form, 'type': 'class_form'})
