from django.contrib import admin
from .models import Personne
from .models import Programme
from .models import Sujet
from .models import Classe
from .models import Enseignant
from .models import Etudiant
from .models import Evaluation

admin.site.register(Personne)
admin.site.register(Enseignant)
admin.site.register(Etudiant)
admin.site.register(Evaluation)
admin.site.register(Programme)
admin.site.register(Sujet)
admin.site.register(Classe)
