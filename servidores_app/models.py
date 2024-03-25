# seu_app/models.py

import uuid
from django.db import models
from cpf_field.models import CPFField
from django.core.exceptions import ValidationError
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import Group

VINCULO_CHOICES = [
        ('contratado', 'Contratado'),
        ('efetivo', 'Efetivo'),
        ('comissionado', 'Comissionado'),
        ('outro', 'Outro'),]

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = CPFField('cpf', unique=True, null=True, error_messages={'unique': 'Já existe um usuário com este CPF. Por favor, escolha outro.'})
    email = models.EmailField(max_length=50, unique=True, null=True, error_messages={'unique': 'Já existe um usuário com este e-mail. Por favor, escolha outro.'})
    telefone = models.CharField(max_length=11)
    instituicao = models.CharField(max_length=50, null=True)
    vinculo = models.CharField(max_length=30, null=True, choices=VINCULO_CHOICES)
    cargo = models.CharField(max_length=30, null=True)
    ch = models.PositiveIntegerField(null=True,default=20)  # Alterado para IntegerField se ch representar carga horária
    rg = models.CharField(max_length=8, null=True)
    org_expedidor = models.CharField(max_length=10, null=True)
    endereco = models.CharField(max_length=100, null=True)
    escolaridade = models.CharField(max_length=50, null=True)
    imagem_perfil = models.ImageField(upload_to='imagens_perfil/', blank=True, null=True)



    def clean(self):
        super().clean()

        # Validar se o campo telefone tem exatamente 11 caracteres numéricos
        if self.telefone and (not self.telefone.isdigit() or len(self.telefone) != 11):
            raise ValidationError('O número de telefone deve conter exatamente 11 dígitos numéricos.')
        
        # Validar se o campo rg tem exatamente 8 caracteres numéricos
        if self.rg and (not self.rg.isdigit() or len(self.rg) != 8):
            raise ValidationError('O número do rg deve conter exatamente 8 dígitos numéricos.')


class CustomUsuario(Usuario):
    pass
    def clean(self):
        super().clean()
        print("Entrou no método clean")  # Adicione esta linha para debug

        # Exemplo de validação personalizada para o campo 'email'
        if CustomUsuario.objects.exclude(pk=self.pk).filter(email=self.email).exists():
            raise ValidationError('Já existe um usuário com este e-mail. Por favor, escolha outro.')

        # Exemplo de validação personalizada para o campo 'cpf'
        if CustomUsuario.objects.exclude(pk=self.pk).filter(cpf=self.cpf).exists():
            raise ValidationError('Já existe um usuário com este CPF. Por favor, escolha outro.')

@receiver(post_delete, sender=Usuario)
def delete_usuario_image(sender, instance, **kwargs):
    # exclua a imagem quando o usuário for excluído
    if instance.imagem_perfil:
        if os.path.isfile(instance.imagem_perfil.path):
            os.remove(instance.imagem_perfil.path)

