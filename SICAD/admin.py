from django.contrib import admin
from .models import Personne
# from .models import Enseignant
from .models import Etudiant
# from .models import Evaluation

admin.site.register(Personne)
# admin.site.register(Enseignant)
admin.site.register(Etudiant)
# admin.site.register(Evaluation)
# Register your models here.
