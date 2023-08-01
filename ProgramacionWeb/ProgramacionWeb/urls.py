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

from centros.views import editarCentro, eliminarCentro
from instalacionesCentros.views import editarInstalacion, eliminarInstalacion
from profesores.views import editarProfesor, eliminarProfesor
from servicios.views import editarServicio, eliminarServicio
from socios.views import editarSocio, eliminarSocio
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
    path('administradorinstalaciones/', administradorInstalaciones, name='administradorinstalaciones'),
    path('administradorservicios/', administradorServicios, name='administradorservicios'),
    path('profesores/', profesores, name='profesores'),
    path('instalaciones/', instalaciones, name='instalaciones'),
    path('servicios/', servicios, name='servicios'),
    path('centros/', centros, name='centros'),
    path('editarCentro/<int:id>', editarCentro, name='editarCentro'),
    path('editarSocio/<int:id>', editarSocio, name='editarSocio'),
    path('editarProfesor/<int:id>', editarProfesor, name='editarProfesor'),
    path('editarInstalacion/<int:id>', editarInstalacion, name='editarInstalacion'),
    path('editarServicio/<int:id>', editarServicio, name='editarServicio'),
    path('eliminarCentro/<int:id>', eliminarCentro, name='eliminarCentro'),
    path('eliminarSocio/<int:id>', eliminarSocio, name='eliminarSocio'),
    path('eliminarProfesor/<int:id>', eliminarProfesor, name='eliminarProfesor'),
    path('eliminarInstalacion/<int:id>', eliminarInstalacion, name='eliminarInstalacion'),
    path('eliminarServicio/<int:id>', eliminarServicio, name='eliminarServicio')
]
