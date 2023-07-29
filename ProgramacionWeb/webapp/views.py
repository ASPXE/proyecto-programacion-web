from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from centros.models import Centros
from instalacionesCentros.models import InstalacionesCentros
from profesores.models import Profesores
from servicios.models import Servicios
from socios.models import Socios


# Create your views here.

def signIn(request):
    # Recuperamos los campos del formulario
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contra = request.POST['contra']

        user = authenticate(username=usuario, password=contra)

        if user is not None:
            #signIn exitoso, entramos al menu de administrador
            login(request, user)
            return render(request, 'FrontEnd/pag/menu.html')
        else:
            # Credenciales incorrectas, redireccionamos al signIn
            messages.error(request, 'Usuario o contraseña incorrecto')
            return redirect('signIn')
    # Regresamos el menu de signIn
    return render(request, 'FrontEnd/pag/index.html')

def signUp(request):
    # Recuperamos los campos del formulario
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contra = request.POST['contra']
        email = request.POST['email']
        # Creamos un objeto de la tabla User
        nuevoUsuario = User.objects.create_user(usuario,email,contra)
        nuevoUsuario.save()
        messages.success(request, "¡Usuario creado exitosamente!")
        # Redireccionamos al signIn
        return redirect('signIn')

    return render(request, 'FrontEnd/pag/registroUsuario.html')

def menu(request):
    return render(request, 'FrontEnd/pag/menu.html')

def socio(request):
    return render(request, 'FrontEnd/pag/socio.html')

def administrador(request):

    # Recuperamos todos los centros de la base de datos
    centros = Centros.objects.all()

    return render(request, 'FrontEnd/pag/administrador.html', {'centros':centros})

def administradorSocio(request):

    # Recuperamos todos los registros de socios de la BD
    socios = Socios.objects.all()

    return render(request, 'FrontEnd/pag/administradorsocio.html', {'socios':socios})

def administradorProfesores(request):

    # Recuperamos todos los profesores de la BD
    profesores = Profesores.objects.all()

    return render(request, 'FrontEnd/pag/administradorprofesores.html', {'profesores':profesores})
def administradorInstalaciones(request):

    # Recuperamos todos los registros de instalacionesCentros
    instalacionesCentros = InstalacionesCentros.objects.all()

    return render(request, 'FrontEnd/pag/administradorinstalaciones.html', {'instalacionesCentros':instalacionesCentros})
def administradorServicios(request):

    # Recuperamos todos los registros de servicios de la BD
    servicios = Servicios.objects.all()

    return render(request, 'FrontEnd/pag/administradorservicios.html', {'servicios':servicios})
def profesores(request):
    return render(request, 'FrontEnd/pag/profesores.html')
def instalaciones(request):
    return render(request, 'FrontEnd/pag/instalaciones.html')

def servicios(request):
    """
    if request.method == 'POST':
        nombre = request.POST['nombreServicio']
        costo = request.POST['costo']

        servicio = Servicios(nombre=nombre, costo=costo)
        servicio.save()
        messages.success(request, '¡Servicio registrado exitosamente!')
        return redirect('servicios')
    """
    return render(request, 'FrontEnd/pag/servicios.html')
def centros(request):
    return render(request, 'FrontEnd/pag/centro.html')


