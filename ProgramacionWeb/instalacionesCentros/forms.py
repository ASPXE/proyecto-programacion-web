from django.forms import ModelForm

from instalacionesCentros.models import InstalacionesCentros


class InstalacionForm(ModelForm):
    class Meta:
        model = InstalacionesCentros
        fields = '__all__'
        widgets = {

        }