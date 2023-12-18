from django.shortcuts import render, get_object_or_404
from users.models import Imobiliaria

def perfilView(request, nome_usuario):
    usuario = get_object_or_404(Imobiliaria, nome=nome_usuario)

    return render(request, 'perfil.html', {'usuario': usuario})