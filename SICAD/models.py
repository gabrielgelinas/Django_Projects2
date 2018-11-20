from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.forms import ModelForm, forms


# region Personne


class Personne(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.TextField(max_length=500, blank=True)
    tel = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username


# region OneToOneFunc


def create_personne(sender, **kwargs):
    if kwargs['created']:
        personne = Personne.objects.create(user=kwargs['instance'])


post_save.connect(create_personne, sender=User)


# endregion
# endregion

# region Etudiant


class Etudiant(models.Model):
    personne = models.OneToOneField(Personne, on_delete=models.CASCADE)
    codePerm = models.TextField(max_length=500, blank=True)
    statut = models.TextField(max_length=500, blank=True)

    def __str__(self):
        if self.codePerm == '':
            return str(self.personne)
        else:
            return self.codePerm


class EtudiantForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'


# endregion

# region Enseignant


class Enseignant(models.Model):
    personne = models.OneToOneField(Personne, on_delete=models.CASCADE)
    codeEnseignant = models.TextField(max_length=500, blank=True)
    etudeMax = models.TextField(max_length=500, blank=True)

    def __str__(self):
        if self.codeEnseignant == '':
            return str(self.personne)
        else:
            return self.codeEnseignant


class EnseignantForm(ModelForm):
    class Meta:
        model = Enseignant
        fields = '__all__'


# endregion

# region Evaluation


class Evaluation(models.Model):
    note1 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    note2 = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    noteFinale = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    presence = models.TextField(max_length=500, blank=True)

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
    programme = models.ForeignKey(Programme, on_delete=models.DO_NOTHING, null=True)
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
    horaire = models.TextField(max_length=200, blank=True)

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
