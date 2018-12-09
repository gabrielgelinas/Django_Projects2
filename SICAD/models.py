from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailField


class UserRegisterForm(UserCreationForm):
    email = EmailField()
    email.label = 'Adresse Courriel'

    # adresse = models.TextField(max_length=500, blank=True)
    # tel = models.TextField(max_length=500, blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     codePerm = models.TextField(max_length=12, blank=True)
#     acces = models.TextField(max_length=20, blank=True)
#     statut = models.TextField(max_length=20, blank=True)
#     codeEnseignant = models.TextField(max_length=10, blank=True)
#     etudeMax = models.TextField(max_length=100, blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class UserPersonneForm(UserCreationForm):
    email = EmailField()
    email.label = 'Adresse Courriel'

    username = UsernameField()
    username.label = 'Utilisateur'

    TypesPersonne = ((1, 'Enseignant'), (2, 'Etudiant'))
    typePersonne = forms.ChoiceField(label='Type de compte', choices=TypesPersonne)

    class Meta:
        model = User
        fields = ['username', 'typePersonne', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # do something with self.cleaned_data['typePersonne']
        username = self.cleaned_data['username']

        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return super(UserPersonneForm, self).save(commit=commit)


#
#
# class UserEtudiantForm(UserCreationForm):
#     email = EmailField()
#     email.label = 'Adresse Courriel'
#
#     username = UsernameField()
#     username.label = 'Utilisateur'
#
#     TypesPersonne = ((1, 'Enseignant'), (2, 'Etudiant'))
#     typePersonne = forms.ChoiceField(label='Type de compte', choices=TypesPersonne,)
#
#     class Meta:
#         model = User
#         fields = ['username', 'typePersonne', 'email', 'password1', 'password2']
#
#     def save(self, commit=True):
#         # do something with self.cleaned_data['typePersonne']
#         username = self.cleaned_data['username']
#
#         if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
#             raise forms.ValidationError(u'Username "%s" is already in use.' % username)
#         return super(UserEtudiantForm, self).save(commit=commit)
#
#
# class UserEnseignantForm(UserCreationForm):
#     email = EmailField()
#     email.label = 'Adresse Courriel'
#
#     username = UsernameField()
#     username.label = 'Utilisateur'
#
#     TypesPersonne = ((1, 'Enseignant'), (2, 'Etudiant'))
#     typePersonne = forms.ChoiceField(label='Type de compte', choices=TypesPersonne)
#
#     class Meta:
#         model = User
#         fields = ['username', 'typePersonne', 'email', 'password1', 'password2']
#
#     def save(self, commit=True):
#         # do something with self.cleaned_data['typePersonne']
#         username = self.cleaned_data['username']
#
#         if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
#             raise forms.ValidationError(u'Username "%s" is already in use.' % username)
#         return super(UserEnseignantForm, self).save(commit=commit)


# region Personne


class Personne(User):
    telephone = models.TextField(max_length=15, blank=True)
    adresse = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.username


# region OneToOneFunc


# def create_personne(sender, **kwargs):
#     if kwargs['created']:
#         newUser = User.objects.get(kwargs['instance'])
#         personne = Personne(content_object=newUser, user=kwargs['instance'])
#         personne.save()
#
#
# post_save.connect(create_personne, sender=User)


# endregion
# endregion


# region Etudiant


class Etudiant(Personne):
    codePerm = models.TextField(max_length=12, blank=True)
    statut = models.TextField(max_length=30, blank=True, default='inactif')

    def __str__(self):
        return self.username


#     if self.username == '':
#         return str('non assigné')
#     else:
#         return self.username

class EtudiantForm(UserCreationForm):
    class Meta:
        model = Etudiant
        fields = ['username', 'email', 'password1', 'password2', 'adresse', 'telephone', 'codePerm']


# endregion

# region Enseignant


class Enseignant(Personne):
    codeEnseignant = models.TextField(max_length=12, blank=True)
    etudeMax = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.username


class EnseignantForm(ModelForm):
    class Meta:
        model = Enseignant
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'adresse', 'telephone', 'codeEnseignant',
                  'etudeMax']


# endregion

# region Evaluation


class Evaluation(models.Model):
    note1 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    note2 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    noteFinale = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    presence = models.TextField(max_length=50, blank=True)

    def __str__(self):
        if self.noteFinale == '':
            return 'No Value'
        else:
            return str(self.noteFinale)


# endregion

# region Programme


class Programme(models.Model):
    codeProgramme = models.TextField(max_length=20, blank=True)
    description = models.TextField(max_length=20, blank=True)

    def __str__(self):
        if self.codeProgramme == '':
            return 'No Value'
        else:
            return str(self.codeProgramme)


class ProgrammeForm(ModelForm):
    class Meta:
        model = Programme
        fields = '__all__'


# endregion

# region Sujet


class Sujet(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.DO_NOTHING)
    codeSujet = models.TextField(max_length=20, blank=True)
    description = models.TextField(max_length=100, blank=True)
    nbCredit = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
    plan = models.TextField(max_length=200, blank=True)
    bibliographie = models.TextField(max_length=200, blank=True)
    preRequis = models.TextField(max_length=200, blank=True)

    def __str__(self):
        if self.codeSujet == '':
            return 'No Value'
        else:
            return str(self.codeSujet)


class SujetForm(ModelForm):
    class Meta:
        model = Sujet
        fields = '__all__'


# endregion

# region Classe


class Classe(models.Model):
    JOUR_SEMAINE = (('L', 'Lundi'), ('M', 'Mardi'), ('M', 'Mercredi'), ('J', 'Jeudi'), ('V', 'Vendredi'))
    SESSION = (('H', 'Hiver'), ('P', 'Printemps'), ('É', 'Été'), ('A', 'Automne'))
    ANNEE = [(n, str(n)) for n in range(2016, 2026)]
    sujet = models.ForeignKey(Sujet, on_delete=models.DO_NOTHING, null=True)
    codeClasse = models.DecimalField(max_digits=3, decimal_places=0, blank=False)
    annee = models.DecimalField(max_digits=4, decimal_places=0, blank=True, choices=ANNEE)
    session = models.TextField(max_length=10, choices=SESSION, blank=False)
    jourSemaine = models.TextField(max_length=10, choices=JOUR_SEMAINE)
    heureDebut = models.TimeField()
    heureFin = models.TimeField()

    def __str__(self):
        if self.codeClasse == '':
            return 'No Value'
        else:
            return str(self.codeClasse)


class ClasseForm(ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'
# endregion


class EtudiantClassForm(forms.Form):

    # here we use a dummy `queryset`, because ModelChoiceField
    # requires some queryset
    class_field = forms.ModelChoiceField(queryset=Classe.objects.all())
    #
    # def __init__(self, classe_id):
    #     super(ClasseForm, self).__init__()
    #     self.fields['class_field'].queryset = Classe.objects.filter(id=classe_id)