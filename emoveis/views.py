from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from users.models import Imobiliaria
from imovel.models import Imovel
from emoveis.utils import mandaEmail
from django.utils import timezone
from django.conf import settings
import random
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')


def loginView(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')

            imobiliaria = Imobiliaria.objects.get(email=email)

            user = authenticate(request, username=imobiliaria.user.username, password=password)

            if user is not None:
                # Login bem-sucedido
                login(request, user)
                return redirect('perfilView', nome_usuario=imobiliaria.nome)
            else:
                # Login falhou
                error_message = "Credenciais inválidas. Tente novamente."
                return render(request, 'login.html', {'error_message': error_message})
        except Exception as e:
            print(f'erro: {e}')
            return render(request, 'login.html', {'error_message': e})
            
    return render(request, 'login.html')


def forgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            usuario = Imobiliaria.objects.get(email=email)
            print(f'Usuário existe: {usuario.nome}')

            token = random.randint(1000, 9999)

            # Adiciona o token e o horario do token no banco
            usuario.token = str(token)
            usuario.token_date = timezone.now()
            usuario.save()

            # mandaEmail(token=token, destinatario=usuario.email, assunto='TOKEN', nome_do_usuario=usuario.nome)
            print(f' --- Token = {token} ---')

            return render(request, 'forgetPassword.html', {'modal_token': True, 'email_usuario': usuario.email})

        except ObjectDoesNotExist:
            return render(request, 'forgetPassword.html', {'modal_token': False, 'msg': 'E-mail não cadastrado!'})

    return render(request, 'forgetPassword.html', {'modal_token': False})

        
def verificaToken(request):
    if request.method == 'POST':
        email_usuario = request.POST.get('email')
        token_form = request.POST.get('token')

        try:
            usuario = Imobiliaria.objects.get(email=email_usuario)

            if token_form == usuario.token:
                tempo_expiracao_token = timezone.timedelta(minutes=settings.TOKEN_LIFETIME)
                diferenca_tempo = timezone.now() - usuario.token_date
                print(diferenca_tempo)
                if diferenca_tempo < tempo_expiracao_token:
                    return render(request, 'redefinirPassword.html', {'email_usuario': usuario.email})
                else:
                    return render(request, 'forgetPassword.html', {'modal_token': True, 'msg': 'Token expirado. Solicite um novo.'})
            else:
                return render(request, 'forgetPassword.html', {'modal_token': True, 'msg': 'Token inválido!'})
        except Imobiliaria.DoesNotExist:
            return render(request, 'forgetPassword.html', {'modal_token': True, 'msg': 'Usuário não encontrado.'})


def redefinirPassword(request):
    email_usuario = request.POST.get('email')
    usuario = Imobiliaria.objects.get(email=email_usuario)

    if request.method == 'POST':
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')

        tempo_expiracao_token = timezone.timedelta(minutes=settings.TOKEN_LIFETIME)
        diferenca_tempo = timezone.now() - usuario.token_date

        if diferenca_tempo > tempo_expiracao_token:
            msg = 'Token expirado!'
            return render(request, 'redefinirPassword.html', {'email_usuario': usuario.email, 'msg': msg})
        
        elif senha2 == senha1:
            # Atualizar senha do usuário
            usuario.user.password = make_password(senha2)
            usuario.user.save()

            # Limpar o token e a data associada
            usuario.token = None
            usuario.token_date = None
            usuario.save()

            messages.success(request, 'Senha redefinida com sucesso. Faça login com a nova senha.')
            return redirect('loginView')
        
        else:
            msg = 'As senhas não são iguais!'
            return render(request, 'redefinirPassword.html', {'email_usuario': usuario.email, 'msg': msg})

    return render(request, 'redefinirPassword.html', {'email_usuario': usuario.email})


def adicionarAnuncioView(request):
    if request.method == 'POST':
        

        residencial = request.POST.get('residencial')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        categoria = request.POST.get('categoria')
        metros_quadrados = request.POST.get('metros_quadrados')
        quartos = request.POST.get('quartos')
        banheiros = request.POST.get('banheiros')
        vagas = request.POST.get('vagas')
        valor = request.POST.get('valor')
        aluguel = request.POST.get('aluguel')
        temporada = request.POST.get('temporada')
        descricao = request.POST.get('descricao')
        
        print(f'residencial ==== {residencial}')
        print(f'cep ==== {cep}')
        print(f'logradouro ==== {logradouro}')
        print(f'bairro ==== {bairro}')
        print(f'cidade ==== {cidade}')
        print(f'estado ==== {estado}')
        print(f'categoria ==== {categoria}')
        print(f'metros_quadrados ==== {metros_quadrados}')
        print(f'quartos ==== {quartos}')
        print(f'banheiros ==== {banheiros}')
        print(f'vagas ==== {vagas}')
        print(f'valor ==== {valor}')
        print(f'aluguel ==== {aluguel}')
        print(f'temporada ==== {temporada}')
        print(f'descricao ==== {descricao}')
        
        
        msg = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'        
        return render(request, 'adicionarAnuncio.html')


    return render(request, 'adicionarAnuncio.html')





###############

def logoutView(request):
    logout(request)
    # messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('index')


def cadastrar_imobiliaria(request):
    if request.method == 'POST':
        # Obtenha os dados do POST
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Verificar se usuario ja existe
        if User.objects.filter(username=username).exists():
            # return render(request, 'cadastrar_usuario.html', {'error': 'Usuário já existe'})

            return redirect('login')

    return render(request, 'cadastrar_usuario.html', {'error': None})

