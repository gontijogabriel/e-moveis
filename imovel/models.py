from django.db import models
from users.models import Imobiliaria


class Imovel(models.Model):

    imobiliaria = models.OneToOneField(Imobiliaria, on_delete=models.CASCADE)
    descricao = models.TextField()
    residencial = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    metros_quadrados = models.PositiveIntegerField(default=0, blank=True, null=True)
    quartos = models.PositiveIntegerField(default=0, blank=True, null=True)
    banheiros = models.PositiveIntegerField(default=0, blank=True, null=True)
    vagas = models.PositiveIntegerField(default=0, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    aluguel = models.BooleanField(default=False)
    temporada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.categoria} - {self.cidade}, {self.estado}"


class FotosImovel(models.Model):
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='imoveis/', blank=True, null=True)

    def __str__(self):
        return f"{self.imovel} - {self.foto}"
    