
from django.shortcuts import render, redirect, get_object_or_404

from centros.forms import CentroForm
from centros.models import Centros

# Create your views here.

#CentroForm = modelform_factory(Centros, exclude=[])
def editarCentro(request, id):
    centro = get_object_or_404(Centros, pk=id)
    if request.method == 'POST':
        formaCentro = CentroForm(request.POST, instance=centro)
        if formaCentro.is_valid():
            formaCentro.save()
            return redirect('editarCentro', id=id)
    else:
        formaCentro = CentroForm(instance=centro)

    return render(request, 'FrontEnd/pag/editarCentro.html', {'formaCentro':formaCentro})

def eliminarCentro(request, id):
    centro = get_object_or_404(Centros, pk=id)
    if centro:
        centro.delete()
    return redirect('administrador')