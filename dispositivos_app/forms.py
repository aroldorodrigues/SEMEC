
from django import forms
from .models import Dispositivo, Documento

class DispositivoForm(forms.ModelForm):

    class Meta:
        model = Dispositivo
        fields = ['status', 'tipo', 'nome_servidor', 'numero_de_serie', 'cpf']

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['arquivo']