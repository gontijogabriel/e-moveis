from django.db import models
from django.contrib.auth.models import User

class Imobiliaria(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.CharField(max_length=255)
    perfil = models.ImageField(upload_to='perfil_imobiliaria/', blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    token_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
