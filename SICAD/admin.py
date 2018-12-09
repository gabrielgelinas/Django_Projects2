from django.contrib import admin
from .models import Personne, EtudiantForm, EnseignantForm
# from .models import Profile
from .models import Programme
from .models import Sujet
from .models import Classe
from .models import Enseignant
from .models import Etudiant
from .models import Evaluation


class EtudiantAdmin(admin.ModelAdmin):
    form = EtudiantForm
    pass


class EnseignantAdmin(admin.ModelAdmin):
    form = EnseignantForm
    pass


class ProgrammeAdmin(admin.ModelAdmin):
    # exclude = ('codeProgramme',)
    pass


admin.site.register(Etudiant, EtudiantAdmin)

admin.site.register(Personne)
admin.site.register(Enseignant, EnseignantAdmin)
admin.site.register(Evaluation)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Sujet)
admin.site.register(Classe)
