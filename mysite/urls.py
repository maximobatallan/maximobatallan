"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from mb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('formulario.html', views.save_formulario, name='save_formulario'),
    path('asistentevirtual.html', views.asistentevirtual, name='asistentevirtual'),
    path('desarrollospersonalizados.html', views.desarrollospersonalizados, name='desarrollospersonalizados'),
    path('exposicionenlinea.html', views.exposicionenlinea, name='exposicionenlinea'),
    path('gestiondelainformacion.html', views.gestiondelainformacion, name='gestiondelainformacion'),
    path('acercadeaev.html', views.acercadeaev, name='acercadeaev'),

]
