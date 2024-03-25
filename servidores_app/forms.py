# nome_do_app/forms.py
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf','email','telefone','instituicao',
                  'vinculo','cargo','ch','rg','org_expedidor',
                  'endereco','escolaridade','imagem_perfil']

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        # Adicione um widget de FileInput para permitir a edição da imagem
        self.fields['imagem_perfil'].widget = forms.FileInput(attrs={'accept': 'image/*'})


