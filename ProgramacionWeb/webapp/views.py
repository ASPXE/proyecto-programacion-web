from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from centros.models import Centros
from codigoPostal.models import CodigoPostal
from colonias.models import Colonias
from estados.models import Estados
from gradoEstudios.models import gradoEstudios
from instalaciones.models import Instalaciones
from instalacionesCentros.models import InstalacionesCentros
from municipios.models import Municipios
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

    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidoP = request.POST['apellidoP']
        apellidoM = request.POST['apellidoM']
        calle = request.POST['calle']
        numExt = request.POST['numExt']
        numInt = request.POST['numInt']
        mensualidad = request.POST['mensualidad']
        cp = request.POST['cp']
        colonia = request.POST['colonia']
        estado = request.POST['estado']
        municipio = request.POST['municipio']

        cp = CodigoPostal.objects.get(pk=cp)
        colonia = Colonias.objects.get(pk=colonia)
        estado = Estados.objects.get(pk=estado)
        municipio = Municipios.objects.get(pk=municipio)

        socio = Socios(nombres=nombre, apellidoP=apellidoP, apellidoM=apellidoM, calle=calle, numExt=numExt, numInt=numInt,
                       mensualidad=mensualidad, cp=cp, colonia=colonia, estado=estado, municipio=municipio)
        socio.save()
        return redirect('socio')


    codigosPostales = CodigoPostal.objects.all()
    colonias = Colonias.objects.all()
    estados = Estados.objects.all()
    municipios = Municipios.objects.all()

    return render(request, 'FrontEnd/pag/socio.html', {'codigosPostales':codigosPostales, 'colonias':colonias,
                                                       'estados':estados, 'municipios':municipios})

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


    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidoP = request.POST['apellidoP']
        apellidoM = request.POST['apellidoM']
        calle = request.POST['calle']
        numExt = request.POST['numExt']
        numInt = request.POST['numInt']
        cp = request.POST['cp']
        municipio = request.POST['municipio']
        colonia = request.POST['colonia']
        estado = request.POST['estado']
        gradoEstudio = request.POST['gradoEstudio']

        cp = CodigoPostal(pk=cp)
        municipio = Municipios(pk=municipio)
        colonia = Colonias(pk=colonia)
        estado = Estados(pk=estado)
        gradoEstudio = gradoEstudios(pk=gradoEstudio)

        profesor = Profesores(nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM, calle=calle,
                              numExt=numExt, numInt=numInt, cp=cp, municipio=municipio, colonia=colonia,
                              estado=estado, gradoEstudios=gradoEstudio)
        profesor.save()
        return redirect('profesores')




    codigosPostales = CodigoPostal.objects.all()
    colonias = Colonias.objects.all()
    estados = Estados.objects.all()
    municipios = Municipios.objects.all()
    gradosEstudios = gradoEstudios.objects.all()

    return render(request, 'FrontEnd/pag/profesores.html', {'codigosPostales':codigosPostales, 'colonias':colonias, 'estados':estados,
                                                            'municipios':municipios, 'gradosEstudios':gradosEstudios})
def instalaciones(request):

    if request.method == 'POST':
        # Obtenemos el ID
        instalacion = request.POST['instalacion']
        centro = request.POST['centro']

        # Recuperamos el objeto de la BD con ayuda del ID
        instalacion = Instalaciones.objects.get(pk=instalacion)
        centro = Centros.objects.get(pk=centro)

        instalacionCentro = InstalacionesCentros(instalacion=instalacion, centro=centro)
        instalacionCentro.save()
        return redirect('instalaciones')

    centros = Centros.objects.all()
    instalaciones = Instalaciones.objects.all()

    return render(request, 'FrontEnd/pag/instalaciones.html', {'centros':centros, 'instalaciones':instalaciones})

def servicios(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        costo = request.POST['costo']

        servicio = Servicios(nombre=nombre, costo=costo)
        servicio.save()
        messages.success(request, "¡Servicio registrado exitosamente!")
        return redirect('servicios')

    return render(request, 'FrontEnd/pag/servicios.html')
def centros(request):

    if request.method == 'POST':
        nombreCentro = request.POST['nombreCentro']
        calle = request.POST['calle']
        numExt = request.POST['numExt']
        numInt = request.POST['numInt']
        """
        Estamos recuperando el ID de lo seleccionado por el usuario, debemos de pasar
        como parametro el objeto
        """
        codigoPostal = request.POST['cp']
        colonia = request.POST['colonia']
        estado = request.POST['estado']
        municipio = request.POST['municipio']

        # Recuperamos el objeto donde el ID es igual al seleccionado en el HTML
        codigoPostal = CodigoPostal.objects.get(pk=codigoPostal)
        colonia = Colonias.objects.get(pk=colonia)
        estado = Estados.objects.get(pk=estado)
        municipio = Municipios.objects.get(pk=municipio)

        centro = Centros(nombre=nombreCentro, calle=calle, numExt=numExt, numInt=numInt, codigoPostal=codigoPostal,
                         colonia=colonia, estado=estado, municipio=municipio)
        centro.save()
        messages.success(request, "¡Centro registrado exitosamente!")
        return redirect('centros')

    # Obtenemos los registros de la base de datos
    codigosPostales = CodigoPostal.objects.all()
    colonias = Colonias.objects.all()
    estados = Estados.objects.all()
    municipios = Municipios.objects.all()

    return render(request, 'FrontEnd/pag/centro.html', {'colonias':colonias, 'estados':estados, 'municipios':municipios, 'codigosPostales':codigosPostales})
