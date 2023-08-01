from django.forms import ModelForm, TextInput

from centros.models import Centros


class CentroForm(ModelForm):
    class Meta:
        model = Centros
        fields = '__all__'
        widgets = {
            'nombreCentro': TextInput(attrs={'type':'text'})
        }