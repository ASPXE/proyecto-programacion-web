from django.shortcuts import render, get_object_or_404, redirect

from instalacionesCentros.forms import InstalacionForm
from instalacionesCentros.models import InstalacionesCentros


# Create your views here.

def editarInstalacion(request, id):
    instalacion = get_object_or_404(InstalacionesCentros, pk=id)
    if request.method == 'POST':
        formaInstalacion = InstalacionForm(request.POST, instance=instalacion)
        if formaInstalacion.is_valid():
            formaInstalacion.save()
            return redirect('editarInstalacion', id=id)
    else:
        formaInstalacion = InstalacionForm(instance=instalacion)
    return render(request, 'FrontEnd/pag/editarInstalacion.html', {'formaInstalacion':formaInstalacion})