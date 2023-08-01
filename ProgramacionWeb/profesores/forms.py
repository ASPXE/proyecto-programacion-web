from django.forms import ModelForm, TextInput

from profesores.models import Profesores


class ProfesorForm(ModelForm):
    class Meta:
        model = Profesores
        fields = '__all__'
        widgets = {
            'nombre':TextInput(attrs={'type':'text'})
        }
