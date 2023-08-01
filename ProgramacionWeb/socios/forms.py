from django.forms import ModelForm, TextInput

from socios.models import Socios


class SocioForm(ModelForm):
    class Meta:
        model = Socios
        fields = '__all__'
        widgets = {
            'nombre':TextInput(attrs={'type':'text'})
        }
