from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def signIn(request):

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
    return render(request, 'FrontEnd/pag/administrador.html')

def profesores(request):
    return render(request,)
def instalaciones(request):
    return render(request,)

def servicios(request):
    return render(request,)
def centros(request):
    return render(request,)


