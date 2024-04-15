from django.db import models

# Escolhas para o tipo de dispositivo
TIPO_CHOICES = [
    ('chromebook', 'Chromebook'),
    ('notebook', 'Notebook')
]

# Escolhas para o status do dispositivo
STATUS_CHOICES = [
    ('estoque', 'Estoque'),
    ('manutencao', 'Manutenção'),
    ('com_servidor', 'Com servidor'),
    ('inativo', 'Inativo')
]

class Dispositivo(models.Model):
    Status = models.CharField(max_length=255, choices=STATUS_CHOICES, blank=True)
    tipo = models.CharField(max_length=255, choices=TIPO_CHOICES, blank=True)
    nome_servidor = models.CharField(max_length=100, blank=True)
    # numero_de_serie = models.CharField(max_length=50, blank=True)
    CPF = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.numero_de_serie

class Documento(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='documentos')
    arquivo = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.arquivo.name