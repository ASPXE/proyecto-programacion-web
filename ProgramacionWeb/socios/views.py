from django.shortcuts import render, get_object_or_404, redirect

from socios.forms import SocioForm
from socios.models import Socios


# Create your views here.

def editarSocio(request, id):
    socio = get_object_or_404(Socios, pk=id)
    if request.method == 'POST':
        formaSocio = SocioForm(request.POST, instance=socio)
        if formaSocio.is_valid():
            formaSocio.save()
            return redirect('editarSocio', id=id)
    else:
        formaSocio = SocioForm(instance=socio)
    return render(request, 'FrontEnd/pag/editarSocios.html', {'formaSocio':formaSocio})

