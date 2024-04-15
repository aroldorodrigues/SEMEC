
from django import forms
from .models import Dispositivo, Documento

class DispositivoForm(forms.ModelForm):

    class Meta:
        model = Dispositivo
        fields = ['Status', 'tipo', 'nome_servidor', 'CPF']

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['arquivo']