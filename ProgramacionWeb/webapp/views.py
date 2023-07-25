from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def logIn(request):

    if request.method == 'POST':
        usuario = request.POST['usuario']
        contra = request.POST['contra']

        user = authenticate(username=usuario, password=contra)

        if user is not None:
            login(request, user)
            return render(request, 'FrontEnd/pag/menu.html')
        else:
            messages.error(request, 'Usuario o contraseña incorrecto')
            return redirect('logIn')

    return render(request, 'FrontEnd/pag/index.html')

def signUp(request):


    #TODO que el equipo de frontend haga el formulario de registro
    return render(request, '')

def menu(request):
    return render(request, 'FrontEnd/pag/menu.html')

def profesores(request):
    return render(request, 'FrontEnd/pag/profesores.html')

def servicios(request):
    return render(request, 'FrontEnd/pag/servicios.html')


def socio(request):
    return render(request, 'FrontEnd/pag/socio.html')


