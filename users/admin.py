# admin.py
from django.contrib import admin
from .models import Imobiliaria

@admin.register(Imobiliaria)
class ImobiliariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'endereco', 'user')
    search_fields = ('nome', 'telefone', 'email', 'endereco', 'user__username', 'user__email')
