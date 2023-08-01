from django.shortcuts import render, get_object_or_404, redirect

from servicios.forms import ServicioForm
from servicios.models import Servicios


# Create your views here.

def editarServicio(request, id):
    servicio = get_object_or_404(Servicios, pk=id)
    if request.method == 'POST':
        formaServicio = ServicioForm(request.POST, instance=servicio)
        if formaServicio.is_valid():
            formaServicio.save()
            return redirect('editarServicio', id=id)
    else:
        formaServicio = ServicioForm(instance=servicio)
    return render(request, 'FrontEnd/pag/editarServicio.html', {'formaServicio':formaServicio})

def eliminarServicio(request, id):
    servicio = get_object_or_404(Servicios, pk=id)
    if servicio:
        servicio.delete()
        return redirect('administradorservicios')