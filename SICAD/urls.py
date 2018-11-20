from django.urls import path
from SICAD.views import views

urlpatterns = [
    path('', views.home, name='sicad-accueil'),
]
