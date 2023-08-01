from django.shortcuts import render, get_object_or_404, redirect

from profesores.forms import ProfesorForm
from profesores.models import Profesores


# Create your views here.

def editarProfesor(request, id):
    profesor = get_object_or_404(Profesores, pk=id)
    if request.method == 'POST':
        formaProfesor = ProfesorForm(request.POST, instance=profesor)
        if formaProfesor.is_valid():
            formaProfesor.save()
            return redirect('editarSocio', id=id)
    else:
        formaProfesor = ProfesorForm(instance=profesor)
    return render(request, 'FrontEnd/pag/editarSocios.html', {'formaSocio': formaProfesor})

def eliminarProfesor(request, id):
    profesor = get_object_or_404(Profesores, pk=id)
    if profesor:
        profesor.delete()
        return redirect('administradorprofesores')

