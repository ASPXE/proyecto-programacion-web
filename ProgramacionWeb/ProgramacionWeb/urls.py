"""
URL configuration for ProgramacionWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from webapp.views import signIn, signUp, menu, socio, administrador, administradorSocio, administradorProfesores, \
    administradorServicios, administradorInstalaciones, instalaciones, centros, profesores, servicios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signIn, name='signIn'),
    path('signUp/', signUp, name='signUp'),
    path('menu/', menu, name='menu'),
    path('socio/', socio, name='socio'),
    path('administrador/', administrador, name='administrador'),
    path('administradorsocio/', administradorSocio, name='administradorsocio'),
    path('administradorprofesores/', administradorProfesores, name='administradorprofesores'),
    path('administradosinstalaciones/', administradorInstalaciones, name='administradorinstalaciones'),
    path('administradorservicios/', administradorServicios, name='administradorservicios'),
    path('profesores/', profesores, name='profesores'),
    path('instalaciones/', instalaciones, name='instalaciones'),
    path('servicios/', servicios, name='servicios'),
    path('centros/', centros, name='centros')
]
