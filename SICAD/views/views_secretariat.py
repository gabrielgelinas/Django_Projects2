from django.shortcuts import render, redirect
from SICAD.models import ClasseForm, ProgrammeForm, SujetForm, UserPersonneForm, Etudiant, Enseignant, EtudiantForm, \
    EnseignantForm, EtudiantClassForm
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    return render(request, 'sicad/secretariat.html')


def create_user_form(request):
    if request.method == 'POST':
        user_form = UserPersonneForm(request.POST)
        if user_form.is_valid():
            type = user_form.cleaned_data.get('typePersonne')  # 1=Enseignant 2=Etudiant

            if type == '1':
                if request.session['acces'] == 'admin':
                    user_form.save()
                    username = user_form.cleaned_data.get('username')
                    newuser = User.objects.get(username=username)
                    type_pers = Enseignant.objects.create()

                    # personne = Personne(content_object=type_pers, user=newuser)
                    # personne.save()
                    messages.success(request, f'Utilisateur {username} created!')
                else:
                    messages.warning(request, f'Vous n\'avez pas les droit pour créer un enseignant.')
                    return render(request, 'sicad/secretariat.html', {'form': user_form, 'type': 'create_user_form'})
            else:
                user_form.save()
                username = user_form.cleaned_data.get('username')
                newuser = User.objects.get(username=username)
                type_pers = Etudiant.objects.create()
                # personne = Personne(content_object=type_pers, user=newuser)
                # personne.save()
                messages.success(request, f'Utilisateur {username} created!')
            return redirect('sicad-secretariat')
    else:
        user_form = UserPersonneForm()
    return render(request, 'sicad/secretariat.html', {'form': user_form, 'type': 'create_user_form'})


def create_etudiant(request):
    if request.method == 'POST':
        etudiant_form = EtudiantForm(request.POST)
        if etudiant_form.is_valid():
            etudiant_form.save()
            description = etudiant_form.cleaned_data.get('description')
            messages.success(request, f'Programme {description} created!')
            return redirect('sicad-secretariat')
    else:
        etudiant_form = EtudiantForm()
    return render(request, 'sicad/secretariat.html', {'form': etudiant_form, 'type': 'etudiant_form'})


def create_enseignant(request):
    if request.method == 'POST':
        enseignant_form = EnseignantForm(request.POST)
        if enseignant_form.is_valid():
            enseignant_form.save()
            description = enseignant_form.cleaned_data.get('description')
            messages.success(request, f'Programme {description} created!')
            return redirect('sicad-secretariat')
    else:
        enseignant_form = EnseignantForm()
    return render(request, 'sicad/secretariat.html', {'form': enseignant_form, 'type': 'enseignant_form'})


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


def etudiant_class_form(request):
    if request.method == 'POST':
        etudiant_class_form = EtudiantClassForm(request.POST)
        if etudiant_class_form.is_valid():
            etudiant_class_form.save()
            # sujet = etudiant_class_form.cleaned_data.get('Sujet')
            # code_classe = etudiant_class_form.cleaned_data.get('codeClasse')
            messages.success(request, f'Etudiant inscrit à la classe : !')
            return redirect('sicad-secretariat')
    else:
        etudiant_class_form = EtudiantClassForm()
    return render(request, 'sicad/secretariat.html', {'form': etudiant_class_form, 'type': 'etudiant_class_form'})
