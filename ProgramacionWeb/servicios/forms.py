from django.forms import ModelForm

from servicios.models import Servicios


class ServicioForm(ModelForm):
    class Meta:
        model = Servicios
        fields = '__all__'
        widgets = {

        }