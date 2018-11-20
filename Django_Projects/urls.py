"""Django_Projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from SICAD.views import views as sicad_views
from SICAD.views import views_secretariat as sicad_views_secretariat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SICAD.urls')),
    path('register/', sicad_views.register, name='register'),
    path('secretariat/create_program/', sicad_views_secretariat.create_program, name='create-program'),
    path('secretariat/create_sujet/', sicad_views_secretariat.create_sujet, name='create-sujet'),
    path('secretariat/create_classe/', sicad_views_secretariat.create_classe, name='create-class'),
    path('secretariat/create_user_form/', sicad_views_secretariat.create_user_form, name='create-user-form'),
    path('', sicad_views.home, name='sicad-accueil'),
    path('secretariat', sicad_views_secretariat.home, name='sicad-secretariat'),
]
