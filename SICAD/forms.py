from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class CreateProgram(forms.Form):
#     code_programme = forms.CharField(label='Code du programme', max_length=100)
#     description = forms.CharField(label='Description', max_length=100)


class CreateSujet(forms.Form):
    code_sujet = forms.DecimalField(label='Code du programme', max_digits=10,decimal_places=0)
    description = forms.CharField(label='Description', max_length=100)
    nb_credit = forms.DecimalField(label='Nombre de crédits', max_digits=2,decimal_places=2)
    plan = forms.CharField(label='Plan', max_length=100)
    bibliographie = forms.CharField(label='Bibliographie', max_length=100)
    prerequis = forms.CharField(label='Pré-requis', max_length=100)
