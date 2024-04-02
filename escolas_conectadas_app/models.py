from django.db import models
from django.core.validators import RegexValidator

class Escolas(models.Model):
    inep = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$', 'O INEP deve ter exatamente 8 dígitos.')])
    nome = models.CharField(max_length = 100)
    status = models.CharField(max_length = 40,blank=True)
    longitude = models.CharField(max_length = 20,blank=True)
    latitude = models.CharField(max_length = 20,blank=True)
    endereco = models.CharField(max_length = 50,blank=True)