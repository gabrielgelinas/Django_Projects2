from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# region Personne
class Personne(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.TextField(max_length=500, blank=True)
    adresse = models.TextField(max_length=500, blank=True)
    tel = models.TextField(max_length=500, blank=True)
    courriel = models.TextField(max_length=500, blank=True)

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
